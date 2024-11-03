#!/usr/bin/env bash
CURL_OUTPUT=$(curl -Gsw"%{http_code}\n" https://jsonplaceholder.typicode.com/posts)
GET_RESPONSE=${CURL_OUTPUT:0:500}
GET_CODE=${CURL_OUTPUT:(-3)}
if [[ $GET_CODE == 200 ]]; then
  echo GET-запрос успешен!
  echo Содержимое страницы:
  echo $GET_RESPONSE
else
  echo Ошибка при GET-запросе: $GET_CODE
fi

CURL_OUTPUT=$(curl -sX POST -d 'title=foo&body=bar&userId=1' -w"%{http_code}\n" https://jsonplaceholder.typicode.com/posts)
POST_RESPONSE=${CURL_OUTPUT:0:500}
POST_CODE=${CURL_OUTPUT:(-3)}
if [[ $POST_CODE == 201 ]]; then
  echo POST-запрос успешен!
  echo Полученные данные:
  echo $POST_RESPONSE
else
  echo Ошибка при POST-запросе: $POST_CODE
fi
