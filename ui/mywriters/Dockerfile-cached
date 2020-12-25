#syntax=docker/dockerfile:experimental

FROM python:3.9-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN echo works!

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip cache list
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY mywriters/poetry.lock mywriters/pyproject.toml /code/

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY mywriters /code/mywriters
WORKDIR /code/mywriters

RUN ln -s /code/mywriters/entrypoint.sh /usr/local/bin/entrypoint.sh
ENTRYPOINT [ "entrypoint.sh" ]
