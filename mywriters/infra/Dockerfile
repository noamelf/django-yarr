FROM python:3.9-slim


ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY infra/poetry.lock infra/pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY mywriters /code/mywriters
WORKDIR /code/mywriters

COPY infra/entrypoint.sh /usr/local/bin/
ENTRYPOINT [ "entrypoint.sh" ]
