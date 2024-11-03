#!/usr/bin/env bash
read -p "Введите IP-адрес: " -re IP
CURL_OUTPUT=$(curl -Gsw"%{http_code}\n" https://ipinfo.io/$IP/json)
GET_RESPONSE=${CURL_OUTPUT:0:-4}
GET_CODE=${CURL_OUTPUT:(-3)}
if [[ $GET_CODE == 200 ]]; then
  #echo $GET_RESPONSE
  IFS='",'
  echo Провайдер: $(echo ${GET_RESPONSE[@]} | grep org | awk '{ $1=$2="";  print $0}' )
  echo Город: $(echo ${GET_RESPONSE[@]} | grep city | awk '{ print $3}' )
  echo Штат: $(echo ${GET_RESPONSE[@]} | grep region | awk '{ print $3}' )
  echo Страна: $(echo ${GET_RESPONSE[@]} | grep country | awk '{ print $3}' )
  # ip :  77.88.44.55  
  # hostname :  yandex.ru  
  # city :  Moscow  
  # region :  Moscow  
  # country :  RU  
  # loc :  55.7522 37.6156  
  # org :  AS208398 Edge Technology Plus d.o.o. Beograd  
  # postal :  101000  
  # timezone :  Europe/Moscow  
  # readme :  https://ipinfo.io/missingauth
  #sed 's/"//g' | awk '{print $2}'
else
  echo Не удалось получить информацию.
fi
