#!/usr/bin/env bash
read -p "Введите адрес хоста для пинга: " -r HOST
ping -c4 $HOST && echo $HOST доступен. || echo $HOST недоступен.
