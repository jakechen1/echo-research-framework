# NAS backup — one-time manual enable

The NAS volume `/Volumes/dataset-jakeclaw` (Synology SMB at
192.168.68.128, 14 TB used / 14 TB free) is mounted but **SSH sessions
cannot write to it due to macOS TCC**. The backup script works fine when
invoked from a Terminal session that has Full Disk Access.

## Enable (one-shot)

1. Open **Terminal.app** on W0 (ssh jakechen@192.168.68.201 via GUI session, or sit at W0)
2. Grant Terminal.app Full Disk Access in System Settings → Privacy & Security
3. Run once:
   ```
   mkdir -p /Volumes/dataset-jakeclaw/phgdh-project
   bash /Users/jakeclaw/workers/bin/nas_backup.sh
   ```
4. (Optional) Schedule hourly via crontab — works from Terminal.app, fails from SSH:
   ```
   crontab -e
   # add:
   0 * * * * /Users/jakeclaw/workers/bin/nas_backup.sh >> /Users/jakeclaw/Library/Logs/nas_backup.log 2>&1
   ```

The scheduler_loop already tries `nas_backup.sh` every 30 min from SSH
(fails silently with TCC denial). Once you run it from Terminal once and
the crontab is set, the permission sticks and subsequent loop-triggered
runs will also succeed.

## Verification

After running, check:
- `cat /tmp/phgdh_nas_summary.json` should show `status: "ok"` + file_count > 0
- Dashboard NAS card will light up with real numbers
