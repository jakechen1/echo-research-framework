#!/bin/bash
# Usage: notify.sh <emoji> <title> [body] [--urgent]
exec /Users/jakeclaw/.hermes-venv/bin/python \
  /Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.py "$@"
