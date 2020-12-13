FROM python:3.7-alpine
MAINTAINER xylo

ENV PYTHONUNBUFFERED 1

COPY ./dependancies.txt /dependancies.txt
RUN pip install -r /dependancies.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app
RUN adduser -D user
USER user


