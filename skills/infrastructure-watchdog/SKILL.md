# Skill: infrastructure-watchdog (diagnostic-only v1)

Probes home + upstream infrastructure every 5 min. Classifies failures.
Notifies with actionable guidance. **No auto-remediation** in v1 —
v2 adds that after we've validated the signal-to-noise ratio.

## Probes

| Signal | Test | Healthy result |
|---|---|---|
| Synology DSM | `nc -zv 192.168.68.128 5000` | open |
| Synology OpenVPN UDP 1194 | LAN-side port probe | open |
| Home router | `nc -zv 192.168.68.1 80` | open |
| Home WAN egress | `curl https://api.ipify.org` on W0 | returns public IP |
| L0 inference | `nc -zv 192.168.68.200 11434` | open |
| Cheaha login | `nc -zv cheaha.rc.uab.edu 22` | open |

## Failure classification

- **DSM ✓ + VPN ✗** → OpenVPN package crashed (Telegram: restart VPN Server from DSM)
- **DSM ✗** → Synology down, physical check (Telegram urgent)
- **Router ✗** → router dead
- **WAN ✗** → ISP outage
- **L0 ✗** → L0 dead/ollama crashed
- **Cheaha ✗** → RC outage or firewall
- **All ✓ locally but UAB can't reach** → UAB egress policy (suggest TCP 443 fallback)

## Output

- `project-state/infra_probe.jsonl` — append per tick
- `/tmp/phgdh_infra_status.json` — latest snapshot for dashboard
- Telegram on status transitions only (not every tick, respects SUPPRESS_ALERTS)

## Not automated (v1)

- Restarting Synology packages (requires DSM API token — deferred to v2)
- Rebooting router (requires smart plug)
- Fixing ISP outages (impossible)
- UAB network policy (impossible)
