FROM docker-proxy.devops.projectronin.io/ronin/base/python-base:1.1.0

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  # Don't use venv with Poetry so we install dependencies globally
  POETRY_VIRTUALENVS_CREATE=false

# Allow for global Poetry Python dependency installs
RUN chown -R ronin:ronin /app /usr/local

RUN apt-get update \
  && apt-get install -y build-essential libpq-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && pip install poetry==1.7.1

USER ronin:ronin

RUN mkdir ./.oci

COPY --chown=ronin:ronin pyproject.toml poetry.lock .
COPY --chown=ronin:ronin infx_semantic_normalization_api infx_semantic_normalization_api

RUN poetry install --without dev

CMD ["python", "-m", "infx_semantic_normalization_api"]
