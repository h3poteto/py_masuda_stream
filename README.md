# MasudaStream

https://masuda-stream.net

## Development

Clone this repository in your computer.

```bash
$ git clone git@github.com:h3poteto/masuda_stream.git
```

```bash
$ cd masuda_stream
$ docker-compose run --rm --service-ports python
Using base prefix '/usr/local'
New python executable in /var/opt/app/bin/python
Installing setuptools, pip, wheel...done.
(app) python@907352e12436:/var/opt/app$
```
Create database:

```bash
$ mysql -u root -h 127.0.0.1
mysql> create database masuda_stream char set utf8mb4;
```

Pip install and migrate:

```bash
(app) python@907352e12436:/var/opt/app$ pip install -r requirements.txt
(app) python@907352e12436:/var/opt/app$ python manage.py migrate
```

After that, run server:

```bash
(app) python@907352e12436:/var/opt/app$ python manage.py runserver 0:8000
```

so, you can access http://localhost:8000 .

## Production
### First setup

Clone this repository.

```bash
$ git clone https://github.com/h3poteto/masuda_stream.git
```

And docker pull.

```bash
$ cd masuda_stream/production
$ docker-compose -f docker-compose.production.yml pull
```

Please set environment variables in your `~/.profile` which is required in `docker-compose.production.yml`.

### Cron

Set cronjob to update entry informations.

```
PATH=/usr/bin:/usr/local/bin/

*/15 * * * * /bin/bash -l -c 'cd /home/docker/masuda_stream/production && docker-compose -f docker-compose.production.yml run --rm rss >> log/rss.log 2>> log/rss.error.log'
```

### Application deploy

```bash
$ cd masuda_stream/production
$ docker stack deploy masuda_stream --compose-file docker-compose.production.yml --with-registry-auth
```
