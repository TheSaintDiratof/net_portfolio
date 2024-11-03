IFS=","
read -p "Введите адрес хоста: " -re HOST
read -p "Введите порты (через запятую): " -re PORTS
for i in $PORTS; do
  nc -z -w 2 $HOST $i 2> /dev/null && AVAIL="$AVAIL$i, "
done
if [[ "$AVAIL" != "" ]]; then
  echo "Открытые порты на $HOST: [${AVAIL:0:-2}]"
else
  echo "Нет открытых портов на $HOST."
fi
