ARG PYTHON_VERSION=3.9

FROM docker-proxy.devops.projectronin.io/python:${PYTHON_VERSION}-slim

EXPOSE 8000

RUN addgroup \
    --system \
    --gid 1000 \
    ronin \
  && adduser \
    --home /app \
    --system \
    --disabled-password \
    --uid 1000 \
    --ingroup ronin \
    ronin \
  && chown -R ronin:ronin /app

RUN apt-get update \
  && apt-get install -y build-essential libpq-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && pip install poetry==1.7.1

USER ronin:ronin

WORKDIR /app

RUN mkdir ./.oci

COPY --chown=ronin:ronin pyproject.toml poetry.lock ./
COPY --chown=ronin:ronin resources/pip.conf .config/pip/
COPY --chown=ronin:ronin infx_mapping_api ./app

RUN poetry install --without dev

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

CMD ["poetry", "run", "python", "-m", "app"]
