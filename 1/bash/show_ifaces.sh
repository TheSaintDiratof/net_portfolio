#!/usr/bin/env bash
for i in /sys/class/net/*; do
  echo Интерфейс: $(basename $i)
  case $(cat $i/link_mode) in
    "0")
      ACTIVE=False
      ;;
    "1")
      ACTIVE=True
      ;;
  esac
  echo "  Активен: $ACTIVE"
  echo "  Скорость: $(cat $i/speed 2> /dev/null || echo 0) Мбит/с"
  case $(cat $i/duplex 2> /dev/null) in
    "unknown")
    DUPLEX=Неизвестно
    ;;
    "half")
    DUPLEX=Полудуплексный
    ;;
    "full")
    DUPLEX=Полный
    ;;
  esac
  echo "  Дуплексный режим: $DUPLEX"
  echo "  MTU: $(cat $i/mtu)"
  echo
done
