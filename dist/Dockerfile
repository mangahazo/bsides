FROM python:slim

RUN apt update
RUN apt install -y gcc g++ libsqlite3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app
WORKDIR /app

EXPOSE 8080

CMD python3 main.py