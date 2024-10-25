# Api para consulta de Criptomoedas

## Descrição

Este projeto é uma API para informações sobre criptomoedas, integrando dados de diferentes provedores como Mercado Bitcoin e CoinGecko. A aplicação é desenvolvida usando **Flask**, e os serviços de banco de dados e cache são gerenciados com **PostgreSQL** e **Redis**, respectivamente.

## Requisitos

Certifique-se de ter os seguintes softwares instalados em sua máquina:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.12](https://www.python.org/)
- [Make](https://www.gnu.org/software/make/) (opcional, mas recomendado)

## Configuração do Ambiente Local

1. Clone este repositório:

   ```bash
   git clone https://github.com/devmateuss/info-coin-api
   cd mercado-bitcoin-project

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

3. Instale as dependências do Python:
    ```bash
    make install

4. Crie um arquivo .env dentro da pasta `app` para armazenar as variáveis de ambiente:
    ```env
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_DB=your_database_name
    SECRET_KEY=962e1cda9a517b53fe1996906f5632cc58e78d35fbabf9dd5433048bf00fa307
    JWT_EXPIRE_MINUTES=60
    REDIS_HOST=localhost
    REDIS_PORT=6379
    REDIS_CACHE_TTL=300

# Como Executar a Aplicação
## Comandos do Makefile
O projeto inclui um `Makefile` para simplificar o gerenciamento de tarefas. Aqui estão os comandos disponíveis:

- ### Iniciar a API localmente
    ```bash
    make api
    
- ### Subir os Contêineres do Banco de Dados e Redis:
    ```bash
    make db

- ### Subir Todos os Serviços com Docker Compose:
    ```bash
    make up

- ### Parar os Contêineres:
    ```bash
    make clean

# Definindo o serviço para consulta de informações
Para consultar as informações das criptomoedas na na rota /api/infocoin você deve passar logo em seguida o provegor por exemplo:
### para acessar a api do mercado bitcoin:
```
/api/infocoin/mercadobitcoin?symbol=btc
```

### para acessar a api da coingecko:
```
/api/infocoin/coingecko?symbol=btc
```

# Acessando a Documentação Swagger
A documentação Swagger estará disponível em:
http://localhost:8000/docs/

# Obter token
Para acessar as rotas você vai precisar de um token que deverar ser passado na requisição como


    Barrear your_token

Você pode fazer a requisição direto do Swagger


# Estrutura do Projeto
```
/mercado-bitcoin-project
├── app/
│   ├── config/            # Configurações do banco de dados e variáveis de ambiente
│   ├── core/              # Lógica central e abstrações
│   │   ├── interfaces/    # Interfaces e classes abstratas para serviços e repositórios
│   ├── common/            # Classes e funções comuns ao projeto, como validações e constantes
│   ├── db/                # Configurações de banco de dados
│   ├── models/            # Modelos SQLAlchemy
│   ├── routes/            # Rotas da API
│   ├── schemas/           # Documentação do Swagger e validação Pydantic
│   ├── scripts/           # Scripts úteis, como a criação de usuários
│   ├── services/          # Lógica de negócios e integrações
│   ├── __init__.py
│   └── main.py            # Arquivo principal para iniciar a aplicação
├── Dockerfile             # Dockerfile para construir a imagem da aplicação
├── app/docker-compose.yml # Docker Compose para gerenciar os contêineres
├── .env                   # Variáveis de ambiente
├── requirements.txt       # Dependências Python
└── README.md              # Documentação do projeto

```
## Documentação da Arquitetura
Para mais informações, consulte a [documentação da Arquitetura](docs/STRUCTURE.md).
