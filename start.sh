#!/bin/bash

while true
do
  hour=$(date -u +"%H")
  if [ "$hour" -ge 8 ] && [ "$hour" -lt 22 ]; then
    echo "⌛ Время в диапазоне — запускаем listener_01.py"
    python3 listener_01.py
  else
    echo "🕒 Не рабочее время (по МСК). Спим 5 мин..."
    sleep 300
  fi
done
