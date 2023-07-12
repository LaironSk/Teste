# TesteAqui está um exemplo de README para o programa e instruções sobre como executá-lo:

# Informações sobre Pacotes Python

Este programa cria um arquivo CSV com informações sobre pacotes Python, obtidas a partir da API do PyPI. Além disso, fornece uma API para acessar essas informações, permitindo a ordenação e busca por nome e versão do Python.

## Requisitos

Para executar o programa, você precisa ter as seguintes dependências instaladas:

- Python 3 (versão 3.6 ou superior)
- Bibliotecas Python: Flask e requests

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

```
pip install flask requests
```

## Como executar o programa

Siga as etapas abaixo para executar o programa:

1. Clone ou faça o download deste repositório para o seu ambiente local.

2. Navegue até o diretório do projeto:

```
cd informacoes-pacotes-python
```

3. Execute o script `gerar_csv.py` para obter as informações dos pacotes e criar o arquivo CSV:

```
python gerar_csv.py
```

Isso irá gerar um arquivo chamado `pacotes.csv` com as informações dos pacotes.

4. Após ter o arquivo CSV criado, execute o script `api.py` para iniciar o servidor da API:

```
python api.py
```

A API será iniciada e estará disponível no endereço `http://localhost:5000/`.

## Rotas da API

A API possui as seguintes rotas:

- `/pacotes`: retorna os pacotes ordenados por nome.
- `/pacotes/nome?nome=<nome_pacote>`: busca pacotes pelo nome.
- `/pacotes/versao_python?versao_python=<versao_python>`: busca pacotes pela versão do Python.

Você pode acessar as rotas acima através de um navegador ou de uma ferramenta como cURL ou Postman.

Certifique-se de substituir `<nome_pacote>` e `<versao_python>` pelos valores desejados ao fazer a busca pelos pacotes.

## Considerações Finais

Este programa é um exemplo básico de como obter informações sobre pacotes Python usando a API do PyPI e fornecer uma API para acessar essas informações. Você pode personalizar e expandir o código de acordo com suas necessidades.

Não se esqueça de tratar adequadamente os erros, implementar autenticação (se necessário) e garantir a segurança da API ao implantá-la em um ambiente de produção.
