# api.limon.sh

### Build

After build service is available on [http://0.0.0.0:8000](http://0.0.0.0:8000)

```bash
$ docker-compose up --build
```

### Migrations

```bash
$ docker-compose run backend python3 manage.py makemigrations <APP_NAME>
```

### Tests

Base tests:

```bash
$ docker-compose run backend pytest tests
```

Test coverage:

```bash
$ docker-compose run backend pytest tests
```


### Linters

Run linter:

```bash
$ docker-compose run backend flake8 apps
```
