FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt