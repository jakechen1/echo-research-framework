#!/bin/bash
# Launch an interactive compute session (for debugging)
# Run from your laptop: bash interactive.sh
# Or adapt the srun command

# CPU interactive (2 hours, 4 cores):
ssh -t cheaha "srun --pty --partition=express --cpus-per-task=4 --mem=8G --time=02:00:00 bash"

# GPU interactive (2 hours, 1 A100):
# ssh -t cheaha "srun --pty --partition=amperenodes --gres=gpu:1 --cpus-per-task=8 --mem=32G --time=02:00:00 bash"
