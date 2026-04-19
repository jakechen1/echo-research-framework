#!/bin/bash
# enqueue_box.sh <src_path> <folder_label> [priority]
SRC="${1:?src required}"; LABEL="${2:?label required}"; PRI="${3:-normal}"
case "$LABEL" in
  root)       FID=377424964160 ;;
  paper)      FID=377423262935 ;;
  slides)     FID=377423558049 ;;
  reports)    FID=377423073347 ;;
  logs)       FID=377424191575 ;;
  data)       FID=377424268363 ;;
  figures)    FID=377423329269 ;;
  references) FID=377424339814 ;;
  *) echo "unknown label: $LABEL"; exit 2 ;;
esac
TS=$(date -u +%FT%TZ)
echo "{\"at\":\"$TS\",\"src\":\"$SRC\",\"folder_id\":\"$FID\",\"folder_label\":\"$LABEL\",\"priority\":\"$PRI\"}" >> /tmp/phgdh_box_pending.json
echo "enqueued $SRC -> box:$LABEL ($FID)"
