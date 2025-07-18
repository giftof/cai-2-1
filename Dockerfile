FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN mv app.py main.py

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80"]
