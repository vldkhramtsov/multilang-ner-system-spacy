FROM python:3.8

RUN apt-get update
RUN python -m pip install --upgrade pip
RUN mkdir app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt
ADD . /app/
