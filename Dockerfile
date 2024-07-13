FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

RUN pip install --upgrade pip
COPY ./ .
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["/bin/sh", "-c", "python manage.py migrate"]


