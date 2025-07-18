PORT=${1:-8080}
COUNT=${2:-100}
URL="http://localhost:${PORT}"

i=1
while [ $i -le $COUNT ]
do
  curl -X POST "$URL" -d "lang=" -d "input_text="
  echo "Request $i sent"
  i=$((i + 1))
done
