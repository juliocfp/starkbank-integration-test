# Transferências PIX com SDK Stark Bank em Python

Este é um projeto em Python que utiliza o SDK do Stark Bank para criar 10 transferências PIX a cada 3 horas durante 24 horas. O objetivo é realizar as requisições de transferências PIX de forma automatizada.

## Requisitos

Para execução do projeto, certifique-se de ter as seguintes dependências instaladas:

SDK do Stark Bank:
```python
pip install starkbank
```
Jinja2:
```python
pip install Jinja2
```
cpf_generator:
```python
pip install cpf_generator
```
names_generator:
```python
pip install names_generator
```

## Configuração

Antes de iniciar a execução do projeto, você precisa de algumas informações importantes:

- Ambiente: Defina o ambiente em que o projeto será executado. Os ambientes possíveis são "sandbox" (ambiente de testes) ou "production" (ambiente de produção).

- ID do Projeto: Forneça o ID do projeto da sua conta na Stark Bank. Esse ID é necessário para autenticar as requisições.

- Private Key: Forneça a chave privada associada ao ID do projeto. Essa chave é utilizada para autenticação nas requisições.

Para saber como criar suas chaves públicas e privadas, e seu ID do projeto, acesse os links:
- https://starkbank.com/docs/api#authentication
- https://github.com/starkbank/ecdsa-python
- https://github.com/starkbank/sdk-python
