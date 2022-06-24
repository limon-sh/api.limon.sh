# api.limon.sh

API service for limon.sh


## Build

You need to create a files for environment variables:
```bash
$ touch .env.local
$ echo "ENVIRONMENT=develop\n\nDJANGO_SETTINGS_MODULE=settings" > .env
```

And build the service containers:
```bash
$ docker-compose up --build
```

After build and up service is available on [http://0.0.0.0:8000](http://0.0.0.0:8000)


## Working with the environment

The service supports working with environments `develop` and `production`.

Environments affect the choice of project configuration file and are set 
via environment variable `ENVIRONMENT` in the file `.env`.

You can also specify application-specific environment variables 
in file `.env.local`.


## Working with the service

You can run commands directly inside the built containers or work with 
the service locally.

The first option is slower, since after each change you have to wait for 
the service in the container to update and restart the server.

Working with the second method is faster, but you will need to install all 
the dependencies on your computer. You will need to install 
[poetry](https://python-poetry.org/docs/#installation) and run the necessary 
services as docker containers:

```bash
$ docker-compose up --detach postgresql redis
$ poetry install
$ poetry shell
(api.limon.sh-py) $ export $(cat .env && cat .env.local)
(api.limon.sh-py) $ cd service
(api.limon.sh-py) service $ python3 manage.py runserver
```


### Migrations

```bash
$ docker-compose run backend python3 manage.py makemigrations <APP_NAME>
```


### Tests

Run tests:

```bash
$ docker-compose run backend pytest
```


### Linters

Run linter:

```bash
$ docker-compose run backend flake8 apps
```
