FROM python:3.6.4-jessie

RUN apt-get update && apt-get install -y g++ make && rm -rf /var/lib/apt/lists/* && pip install --upgrade ortools

WORKDIR /app

ADD . .
