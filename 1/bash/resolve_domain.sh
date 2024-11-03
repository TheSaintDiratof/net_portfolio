#!/usr/bin/env bash
read -p "Введите доменное имя: " -re HOST
IP=$(host $HOST | grep address | awk '{print $4}' | head -n1)

if [[ "$IP" == "" ]]; then
  echo "Не удалось разрешить доменное имя $HOST."
else
  echo "IP-адрес $HOST: $IP"
fi
