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

## Importação dos dados para a imagem docker

```bash
$ docker cp ./assets/projectFile.json ce43f043004c:projectFile.json
$ docker exec ce43f043004c mongoimport -d project -c listing --file projectFile.json
```