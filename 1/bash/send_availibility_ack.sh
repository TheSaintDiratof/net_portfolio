# Нужно внести не достающие данные вместо ххх
read -p "Введите адреса хостов для мониторинга (через запятую): " -re HOSTS
source ~/secrets

while true; do 
  for i in $HOSTS; do
    if ping -c1 $i; then
      echo $i доступен.
      echo "To: $RCPT_EMAIL" >> email.txt
      echo "Subject: Хост $i доступен" >> email.txt
      echo "From: $SNDR_EMAIL" >> email.txt
      echo Content-Type: text/plain\; charset=\"utf-8\" >> email.txt
      echo "Хост $i доступен для подключения." >> email.txt
      curl -s --url 'smtps://smtp.bk.ru:465' --ssl-reqd --mail-from "$SNDR_EMAIL" \
      --mail-rcpt "$RCPT_EMAIL" --upload-file email.txt \
      --user "$SNDR_EMAIL:$PASSWD" \
      && echo Уведомление отправлено на $RCPT_EMAIL о доступности $HOST. \
      || echo Не удалось отправить уведомление.
      rm email.txt
    else
      echo $i недоступен.
    fi
  done
  sleep 5
done

