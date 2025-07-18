FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "david.main:app", "--bind", "0.0.0.0:80", "-w", "2", "--worker-class", "gevent"]
