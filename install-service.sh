#!/bin/bash
set -e

SERVICE_NAME=fridge_door.service
PROJECT_DIR="/home/raspberry5/fridge_door"
SERVICE_PATH="$PROJECT_DIR/$SERVICE_NAME"
INSTALL_PATH="/etc/systemd/system/$SERVICE_NAME"
SCRIPT_PATH="$PROJECT_DIR/fridge_door.sh"

if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run with sudo."
  echo "Usage: sudo $0"
  exit 1
fi

cp "$SERVICE_PATH" "$INSTALL_PATH"
chmod 644 "$INSTALL_PATH"
chmod +x "$SCRIPT_PATH"

systemctl daemon-reload
systemctl enable "$SERVICE_NAME"
systemctl restart "$SERVICE_NAME"

echo "Installed and started $SERVICE_NAME"
