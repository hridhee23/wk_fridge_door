#!/bin/bash
set -e

cd /home/raspberry5/fridge_door/src

if [ -x "/home/raspberry5/fridge_door/venv/bin/python" ]; then
  exec "/home/raspberry5/fridge_door/venv/bin/python" main.py
else
  exec python3 main.py
fi
