ARG PYTHON_VERSION=3.9

FROM docker-proxy.devops.projectronin.io/python:${PYTHON_VERSION}-slim

EXPOSE 5000

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

WORKDIR /app

COPY --chown=ronin:ronin pyproject.toml ./
COPY --chown=ronin:ronin poetry.lock ./

USER ronin:ronin

RUN poetry install

COPY --chown=ronin:ronin infx_mapping_api ./app

RUN mkdir ./.oci

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# While Flask App is in dev mode, need to set the host for external visibility
CMD ["poetry", "run", "flask", "--app", "app.app", "run", "--host", "0.0.0.0"]
