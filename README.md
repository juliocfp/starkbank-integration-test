# Transferências PIX com SDK Stark Bank em Python

Este é um projeto em Python que utiliza o SDK do Stark Bank para criar 10 transferências PIX a cada 3 horas durante 24 horas. O objetivo é realizar as requisições de transferências PIX de forma automatizada.

## Requisitos

Além de ter instalado o Python 3.x na máquina para execução do projeto, certifique-se de ter as seguintes dependências instaladas:

SDK do Stark Bank:
```
pip install starkbank
```
Jinja2:
```
pip install Jinja2
```
cpf_generator:
```
pip install cpf_generator
```
names_generator:
```
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

## Execução

Para executar, rode o seguinte comando:
```
python run.py <ambiente> <id_do_projeto> '<conteudo_chave_privada>'
```
Substitua <ambiente>, <id_do_projeto> e <conteudo_chave_privada> pelos valores correspondentes de acordo com a sua configuração.
Exemplo:
```
python run.py sandbox 012938476125 '-----BEGIN EC PARAMETERS----- UioobiuBOg== -----END EC...'
```

## Funcionamento
Ao ser executado, o projeto iniciará um processo de criação de 10 transferências PIX a cada 3 horas durante 24 horas. Para cada transferência, o programa irá gerar automaticamente um nome aleatório e um CPF válido utilizando as bibliotecas names_generator e cpf_generator, respectivamente.

## Relatório
Após a execução, o projeto irá gerar um relatório com as seguintes informações:

- Porcentagem de Transferências com Sucesso: O porcentual de transferências que foram concluídas com sucesso em relação ao total de transferências realizadas.

- Média de Tempo de Processamento: O tempo médio que levou desde a criação da transferência até o último log de sucesso ou falha.

- Possíveis Erros: Caso alguma transferência tenha falhado, o relatório exibirá os possíveis erros que podem ter acontecido durante o processo.

O relatório será gerado na raiz do projeto no formato html.
