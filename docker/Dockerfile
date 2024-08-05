FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y python3-dev gcc libc-dev libffi-dev libpq-dev

RUN useradd --system app && \
    mkdir /app && \
    chown app:app /app &&\
    su app

COPY poetry.lock pyproject.toml /app/

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /app/

RUN chmod +x /app/docker/server-entrypoint.sh
