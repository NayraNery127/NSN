# Arquitetura

O projeto é organizado em **camadas**. Cada camada tem uma única responsabilidade e só conversa com a camada vizinha.

## Fluxo de uma requisição

```
Cliente (Postman / navegador)
        │
        ▼
   Rota (server.py) ◄── Schema (validação)
        │
        ▼
   Repositório (acesso aos dados)
        │
        ▼
   Model ──► Banco de dados (banco_nsn.db)
```

1. O **cliente** envia uma requisição HTTP
2. A **rota** recebe o pedido
3. O **schema** valida os dados recebidos
4. A rota chama o **repositório**
5. O repositório usa o **model** para ler ou gravar no **banco**
6. A resposta volta ao cliente em JSON, com o status code

## Estrutura de pastas

```
src/
├── server.py                       # rotas da API
├── schema/
│   └── schemas.py                  # validação dos dados (Pydantic)
└── infra/sqlalchemy/
    ├── config/database.py          # conexão com o banco
    ├── models/models.py            # tabelas do banco
    └── repositorios/produto.py     # acesso ao banco (CRUD)
```

## Responsabilidade de cada camada

| Camada | Arquivo | Responsabilidade |
|---|---|---|
| **Rota** | `server.py` | recebe o pedido e chama o repositório |
| **Schema** | `schemas.py` | valida os dados que entram e saem da API |
| **Repositório** | `produto.py` | é a única camada que acessa o banco |
| **Model** | `models.py` | define as tabelas do banco |
| **Configuração** | `database.py` | faz a conexão com o banco |

## Schema x Model

São parecidos, mas têm papéis diferentes:

- **Schema (Pydantic):** o formato do dado que **entra e sai da API**
- **Model (SQLAlchemy):** o formato do dado **guardado no banco**
