#!/bin/bash
# Infrastructure probe — every 5 min from scheduler
set -u
OUT_JSONL=$HOME/.openclaw/workspace/project-state/infra_probe.jsonl
SNAP=/tmp/phgdh_infra_status.json
PREV=/tmp/phgdh_infra_prev.json
TS=$(date -u +%FT%TZ)
NOTIFY=$HOME/.openclaw/workspace/skills/notifier/scripts/notify.sh

probe() {
  local host=$1 port=$2
  nc -zv -G 3 "$host" "$port" 2>&1 | grep -q succeeded && echo ok || echo fail
}
probe_udp() {
  local host=$1 port=$2
  nc -zu -G 3 "$host" "$port" 2>&1 | grep -q succeeded && echo ok || echo unknown
}

DSM=$(probe 192.168.68.128 5000)
VPN=$(probe_udp 192.168.68.128 1194)
ROUTER=$(probe 192.168.68.1 80)
L0=$(probe 192.168.68.200 11434)
CHEAHA=$(probe cheaha.rc.uab.edu 22)
WAN_IP=$(curl -s --max-time 4 https://api.ipify.org 2>/dev/null)
WAN=$([ -n "$WAN_IP" ] && echo ok || echo fail)

# Classify
STATUS=healthy
SUMMARY="all systems nominal"
if [ "$ROUTER" = "fail" ]; then STATUS=router_down; SUMMARY="home router not responding at 192.168.68.1"
elif [ "$WAN" = "fail" ]; then STATUS=wan_down; SUMMARY="no internet from W0 — ISP outage likely"
elif [ "$DSM" = "fail" ]; then STATUS=synology_down; SUMMARY="Synology DSM unreachable — check power/storage"
elif [ "$VPN" = "fail" ] && [ "$DSM" = "ok" ]; then STATUS=vpn_package_down; SUMMARY="Synology alive but OpenVPN not listening — open DSM → VPN Server → Run"
elif [ "$L0" = "fail" ]; then STATUS=l0_down; SUMMARY="L0 unreachable — ollama crashed or L0 rebooting"
elif [ "$CHEAHA" = "fail" ]; then STATUS=cheaha_unreachable; SUMMARY="Cheaha login port closed — RC outage?"
fi

cat > $SNAP <<EOF
{
  "at": "$TS",
  "status": "$STATUS",
  "summary": "$SUMMARY",
  "probes": {
    "synology_dsm":    "$DSM",
    "synology_vpn":    "$VPN",
    "home_router":     "$ROUTER",
    "home_wan":        "$WAN",
    "home_wan_ip":     "$WAN_IP",
    "l0_inference":    "$L0",
    "cheaha_login":    "$CHEAHA"
  }
}
EOF
chmod 644 $SNAP
mkdir -p $(dirname $OUT_JSONL)
echo "{\"at\":\"$TS\",\"status\":\"$STATUS\",\"DSM\":\"$DSM\",\"VPN\":\"$VPN\",\"ROUTER\":\"$ROUTER\",\"WAN\":\"$WAN\",\"L0\":\"$L0\",\"CHEAHA\":\"$CHEAHA\"}" >> $OUT_JSONL

# Notify only on transitions
PREV_STATUS=healthy
[ -f $PREV ] && PREV_STATUS=$(cat $PREV 2>/dev/null)
if [ "$STATUS" != "$PREV_STATUS" ]; then
  if [ "$STATUS" = "healthy" ] && [ "$PREV_STATUS" != "healthy" ]; then
    bash $NOTIFY "✅" "Infra recovered: $PREV_STATUS → healthy" "$SUMMARY" >/dev/null 2>&1
  else
    urgent=""
    case $STATUS in synology_down|router_down|wan_down) urgent="--urgent" ;; esac
    bash $NOTIFY "⚠️" "Infra: $STATUS" "$SUMMARY" $urgent >/dev/null 2>&1
  fi
  echo "$STATUS" > $PREV
fi
