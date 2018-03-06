FROM node:9-alpine AS frontend

ENV APP_DIR /var/opt/app

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

RUN set -x \
    && npm install \
    && npm run release-compile


FROM h3poteto/python:3.6.4

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    rm -rf /var/lib/apt/lists/*

ENV APP_DIR /var/opt/app
ENV DJANGO_ENV prod

COPY --chown=python:python . ${APP_DIR}
COPY --chown=python:python --from=frontend /var/opt/app/webpack-stats.json ${APP_DIR}/webpack-stats.json
COPY --chown=python:python --from=frontend /var/opt/app/public ${APP_DIR}/public

USEr python

RUN set -x \
    && pip install -r requirements.txt --user \
    && python manage.py compilemessages \
    && python manage.py collectstatic

EXPOSE 8000:8000

CMD uwsgi --http :8000 --module masuda_stream.wsgi --static-map /static=${APP_DIR}/static
