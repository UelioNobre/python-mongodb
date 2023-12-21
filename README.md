# python-mongodb

## Executando o container Docker
```bash
docker compose -f "docker-compose.yaml" up -d --build
```

## Executando ambiente virtual Python
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

## Encerrar ambiente virtual Python
```bash
$ deactivate
```


## Exportando dependencias utilizadas com freeze
```bash
$ python -m pip freeze > requirements.txt
```