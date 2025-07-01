#!/bin/bash

HOUR=$(date +%H)
if [ "$HOUR" -ge 11 ] || [ "$HOUR" -lt 1 ]; then
    echo "✅ Время в пределах 11:00–01:00. Запускаем парсер..."
    python listener_01.py
else
    echo "⏳ Сейчас не время работы парсера. Завершаем..."
    exit 0
fi
