#!/bin/bash

export AWS_DEFAULT_REGION=ap-northeast-1

myaws ssm parameter get masudastream.$SERVICE_ENV.django_env --region $AWS_DEFAULT_REGION
ret=$?
if [[ $ret -ne 0 ]]; then
    exit
fi

export DJANGO_ENV=`myaws ssm parameter get masudastream.$SERVICE_ENV.django_env --region $AWS_DEFAULT_REGION`
export DJANGO_LOG_LEVEL=`myaws ssm parameter get masudastream.$SERVICE_ENV.django_log_level --region $AWS_DEFAULT_REGION`
export SECRET_KEY=`myaws ssm parameter get masudastream.$SERVICE_ENV.secret_key --region $AWS_DEFAULT_REGION`
export DB_HOST=`myaws ssm parameter get masudastream.$SERVICE_ENV.db_host --region $AWS_DEFAULT_REGION`
export DB_USER=`myaws ssm parameter get masudastream.$SERVICE_ENV.db_user --region $AWS_DEFAULT_REGION`
export DB_NAME=`myaws ssm parameter get masudastream.$SERVICE_ENV.db_name --region $AWS_DEFAULT_REGION`
export DB_PASSWORD=`myaws ssm parameter get masudastream.$SERVICE_ENV.db_password --region $AWS_DEFAULT_REGION`
export SLACK_TOKEN=`myaws ssm parameter get masudastream.$SERVICE_ENV.slack_token --region $AWS_DEFAULT_REGION`
export SLACK_CHANNEL=`myaws ssm parameter get masudastream.$SERVICE_ENV.slack_channel --region $AWS_DEFAULT_REGION`
# pip install --userのインストール先をパスに追加する必要がある
export PATH=$PATH:/home/python/.local/bin

exec "$@"
