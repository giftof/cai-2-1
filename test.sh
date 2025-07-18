#!/bin/bash

PORT=${1:-8080}         # 기본 포트 8080
COUNT=${2:-100}         # 기본 요청 수 100
CONCURRENCY=${3:-10}    # 기본 동시 요청 수 10
URL="http://localhost:${PORT}"

echo "Sending $COUNT requests to $URL with concurrency=$CONCURRENCY"

i=1
while [ $i -le $COUNT ]
do
  for ((j=0; j<$CONCURRENCY && i<=$COUNT; j++, i++))
  do
    curl -s -X POST "$URL" -d "lang=en" -d "input_text=a" > /dev/null &
    echo "Request $i sent"
  done
  wait  # 현재 실행된 백그라운드 curl들이 끝날 때까지 대기
done
