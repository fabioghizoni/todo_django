FROM python:3.7-alpine

WORKDIR /todo_django

COPY . /todo_django

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps \
    && apk add libpq
