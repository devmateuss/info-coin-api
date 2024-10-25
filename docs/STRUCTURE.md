# Arquitetura e Estratégias do Projeto

## Visão Geral

Este projeto é uma API para informações sobre criptomoedas, projetada para ser extensível e escalável. A arquitetura foi desenvolvida seguindo os princípios da **Clean Architecture**, garantindo uma clara separação de responsabilidades entre os diferentes componentes e camadas da aplicação.

## Estrutura da Arquitetura

A arquitetura está organizada em várias camadas, cada uma com responsabilidades específicas. Aqui estão as principais pastas e suas funções:
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


## Princípios de Arquitetura

### Clean Architecture

A **Clean Architecture** foi escolhida para este projeto com o objetivo de criar uma aplicação flexível e fácil de manter, seguindo os seguintes princípios:

- **Separação de Responsabilidades**: Cada camada tem um propósito claro, o que facilita a manutenção e a evolução do projeto.
- **Dependência Inversa**: As camadas de negócios (regras de negócio e lógica) não dependem diretamente de frameworks ou tecnologias específicas. Isso permite trocar um serviço ou uma tecnologia sem alterar a lógica central da aplicação.
- **Facilidade de Testes**: Com a lógica de negócios separada em `services` e `repositories`, é fácil criar testes unitários para cada parte do sistema.

### Estratégia de Integração com APIs Externas

O projeto integra dados de múltiplos provedores de criptomoedas (e.g., Mercado Bitcoin, CoinGecko). A integração segue uma abordagem modular:

- **Interfaces e Repositórios**: A camada de `core/interfaces` define contratos para os repositórios e serviços que devem ser implementados. Isso facilita a adição de novos provedores sem alterar a lógica existente.
- **Service Factory**: Utilizamos uma factory para criar instâncias de serviços com base no provedor especificado. Isso permite trocar de provedor dinamicamente conforme a necessidade, mantendo um ponto único de mudança.

### Gerenciamento de Dependências

- **Pydantic**: Utilizado para validação de dados e definição de schemas. Isso garante que os dados sejam validados antes de serem processados pela API.
- **SQLAlchemy**: Usado como ORM para gerenciar a persistência no banco de dados PostgreSQL.
- **Redis**: Implementado para cache de respostas, acelerando a recuperação de dados e diminuindo o número de requisições às APIs externas.

## Estratégia de Autenticação

A autenticação é feita usando **JWT (JSON Web Tokens)**:

- **Geração de Tokens**: O serviço de autenticação (`AuthenticationService`) gera tokens JWT ao validar credenciais de login.
- **Proteção de Endpoints**: Alguns endpoints exigem que o usuário forneça um token válido no cabeçalho de autorização (`Authorization: Bearer {token}`).
- **Expiração Configurável**: O tempo de expiração dos tokens é definido pela variável `JWT_EXPIRE_MINUTES` no `.env`, garantindo flexibilidade na configuração.

## Organização dos Arquivos

### `core/interfaces`

Contém as interfaces que definem os contratos de repositórios e serviços. Por exemplo:

- `BaseUserRepository`: Define os métodos que um repositório de usuários deve implementar, como `get_user_by_username` e `create_user`.
- `BaseCryptoService`: Define os métodos que um serviço de criptomoedas deve implementar, como `get_coin_info`.

### `services`

Contém a lógica de negócios e integrações:

- **`AuthenticationService`**: Responsável pela autenticação e manipulação de tokens JWT.
- **`CoinService`**: Responsável por integrar com os provedores de dados de criptomoedas e aplicar a lógica de negócio.

### `repositories`

Implementações dos repositórios que interagem com o banco de dados ou APIs externas. Seguem as interfaces definidas em `core/interfaces`.

### `routes`

Define os endpoints expostos pela API. As `routes` são responsáveis apenas por delegar as requisições aos `services` e `repositories`, sem conter lógica de negócios.

## Docker e Docker Compose

- **Dockerfile**: Usado para criar uma imagem da aplicação, configurada para ser leve e eficiente.
- **Docker Compose**: Gerencia os contêineres da aplicação, banco de dados PostgreSQL e Redis. O arquivo `docker-compose.yml` está localizado dentro da pasta `app` e é referenciado diretamente pelo `Makefile`.

### Comandos do Makefile

O `Makefile` facilita o uso de comandos para configurar e rodar o projeto. Os principais comandos são:

- `make api`: Inicia a aplicação Flask localmente.
- `make db`: Inicia apenas o banco de dados e o Redis.
- `make up`: Constrói e inicia todos os serviços definidos no `docker-compose.yml`.
- `make down`: Para e remove todos os contêineres.
- `make clean`: Limpa recursos não utilizados do Docker, como contêineres, imagens e volumes.

## Conclusão

A arquitetura do projeto foi desenhada para ser modular, escalável e fácil de manter. Com a **Clean Architecture** e uma estrutura bem definida, é possível adicionar novos provedores de dados, expandir as funcionalidades da API e adaptar a aplicação a diferentes necessidades de forma simples.

Para mais detalhes ou sugestões, fique à vontade para explorar a documentação ou contribuir com o projeto.
