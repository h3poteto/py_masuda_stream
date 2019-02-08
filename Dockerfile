FROM node:9-alpine AS frontend

ENV APP_DIR /var/opt/app

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

RUN set -x \
    && npm install \
    && npm run release-compile


FROM h3poteto/python:3.6.4

USER root

ENV APP_DIR /var/opt/app
ENV DJANGO_ENV prod

COPY --chown=python:python . ${APP_DIR}
COPY --chown=python:python --from=frontend /var/opt/app/webpack-stats.json ${APP_DIR}/webpack-stats.json
COPY --chown=python:python --from=frontend /var/opt/app/public ${APP_DIR}/public

RUN set -x \
    && curl -fsSL https://github.com/minamijoyo/myaws/releases/download/v0.3.0/myaws_v0.3.0_linux_amd64.tar.gz \
    | tar -xzC /usr/local/bin && chmod +x /usr/local/bin/myaws

USER python
WORKDIR ${APP_DIR}

RUN set -x \
    && pip install -r requirements.txt --user \
    && python manage.py compilemessages \
    && python manage.py collectstatic

EXPOSE 8000:8000

ENTRYPOINT ["entrypoint.sh"]

CMD uwsgi --ini uwsgi_prod.ini
