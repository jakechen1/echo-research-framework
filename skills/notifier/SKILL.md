# Skill: notifier

Sends proactive Telegram notifications to the user when major milestones occur.
Uses the existing bot token at `~/.openclaw/openclaw.json` (channels.telegram.botToken)
to chat_id 8156711151.

## Events that notify (severity-tagged)

| Event                           | Severity | Source                       |
|---------------------------------|----------|------------------------------|
| Subtask / Task completed        | 🎯       | `promote_next_goal.sh`       |
| PLEASER stage transition        | 🔄       | iteration_state writers      |
| Iteration closed (AGE scored)   | 🏆       | `age_score.py` (score ≥ 7)   |
| Achievement (any axis ≥ 8)      | 🏆       | `age_score.py`               |
| Resolver alert (any red channel)| 🚨       | `liveness.sh --resolver`     |
| New Aim started                 | 🚀       | `promote_next_goal.sh`       |
| Wiki published                  | 📚       | `phgdh_publish.sh`           |
| Scavenger ran (delta > 100)     | 📊       | `phgdh_scavenger.py`         |
| Parallel dispatch done          | ⚡       | `go_full_speed.sh`           |

## Invocation

```
# Direct:
bash skills/notifier/scripts/notify.sh "🎯 Task 2.1 done" "n=1011 mean=5.995"

# Python lib:
from notifier import notify
notify("🚨", "Resolver alert", "red: dashboard_api, box_sync")

# Dedup: same (emoji,title) within 10 min is suppressed.
```

## Rate-limits
- Max 1 msg / 5 s
- Max 20 msgs / hour
- Dedup window: 600 s on (emoji + title) hash
