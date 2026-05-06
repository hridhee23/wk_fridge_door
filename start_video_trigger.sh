#!/bin/bash
set -e

cd /home/raspberry5/video_trigger_project/src

if [ -x "/home/raspberry5/video_trigger_project/venv/bin/python" ]; then
  exec "/home/raspberry5/video_trigger_project/venv/bin/python" main.py
else
  exec python3 main.py
fi
