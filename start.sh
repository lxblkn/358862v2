#!/bin/bash

while true; do
  hour=$(TZ="Europe/Moscow" date +%H)
  if [ "$hour" -ge 11 ] || [ "$hour" -lt 1 ]; then
    echo "🟢 Starting parser..."
    python3 listener_01.py
  else
    echo "⏸ Outside working hours (MSK), sleeping 5 minutes..."
    sleep 300
  fi
done
