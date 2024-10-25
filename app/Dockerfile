FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV FLASK_ENV=production
ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
