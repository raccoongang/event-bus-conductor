FROM python:3.8-slim-bullseye as base

ENV PYTHONUNBUFFERED 1
RUN apt update -y && apt install make

WORKDIR /app

FROM base as tester

COPY requirements/test.txt requirements/test.txt
RUN pip install -r requirements/test.txt


FROM base as packer

COPY requirements/pypi.txt requirements/pypi.txt
RUN pip install -r requirements/pypi.txt
