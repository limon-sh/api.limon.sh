FROM python:3.10-slim


ARG APP_PATH=/app
ARG APP_USER=appuser

RUN apt-get update -y && apt-get install -y curl

RUN groupadd --system ${APP_USER} && \
    useradd --no-create-home -u 1000 -r -g ${APP_USER} ${APP_USER}

WORKDIR ${APP_PATH}

COPY --chown=${APP_USER}:${APP_USER} service/ ${APP_PATH}/

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install $(test "$ENVIRONMENT" = "production" && echo "--no-dev") --no-interaction

USER ${APP_USER}:${APP_USER}

CMD python3 manage.py migrate && \
    python3 manage.py collectstatic --no-input && \
    python3 manage.py runserver 0.0.0.0:80
#	gunicorn --worker-class=gthread -b 0.0.0.0:80 wsgi:application
