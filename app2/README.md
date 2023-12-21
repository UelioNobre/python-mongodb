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

## Importação de arquivos para máquina virtual Docker
```bash
$ docker cp "nome-do-arquivo" "container ou id":"diretório destino"
```

## Usando `mongoimport` para importar dados (_image docker_)

A ferramenta "mongoimport" importa conteúdo de uma exportação "JSON estendido", CSV ou TSV criada por "mongoexport" ou, potencialmente, outra ferramenta de exportação de terceiros.

Os parâmetros utilizados neste documentos:
 - `-d`
  Especifica o nome do banco de dados no qual será executado o "mongoimport".Alternativamente, você também pode especificar o banco de dados diretamente na "string de conexão URI".Fornecer uma cadeia de conexão ao mesmo tempo que usa "--db" e especifica informações conflitantes resultará em um erro.
 - `-c`
  Especifica a coleção a ser importada. Se você não especificar "--collection", "mongoimport" lerá o nome da coleção do nome do arquivo de entrada, omitindo a extensão do arquivo, se houver.
 - `--file`
  Especifica o local e o nome de um arquivo que contém os dados a serem importados. Se você não especificar um arquivo, o mongoimport lerá os dados da entrada padrão (por exemplo, "stdin").

 - `--jsonArray`
 Aceita a importação de dados expressos com vários documentos MongoDB em um único array JSON. Limitado a importações de 16 MB ou menos.

```bash
mongoimport -d "nome-do-banco-de-dados" -c 'nome-da-collection' --file "endereço/do/arquivo.json" --jsonArray
```

## Usando `mongoimport` para importar dados (_host terminal_)

```bash
$ docker exec "nome da imagem" mongoimport -d "nome-do-banco-de-dados" -c 'nome-da-collection' --file "endereço/do/arquivo.json" --jsonArray
```


## Importação do arquivo de exemplo

```bash
$docker cp ./assets/projectFile.json banco_de_dados_python_mongo_app2:projectFile.json

$docker exec banco_de_dados_python_mongo_app2 mongoimport -d project -c listing --file projectFile.json
```
