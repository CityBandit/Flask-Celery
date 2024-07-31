FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

COPY app.py /app/