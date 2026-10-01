# Banco de dados

O projeto usa **SQLite**, um banco de dados em arquivo (`banco_nsn.db`), criado automaticamente na primeira execução.

A comunicação é feita pelo **SQLAlchemy**, um ORM: o código é escrito em Python e o SQLAlchemy gera o SQL correspondente.

## Configuração

A configuração da conexão segue o padrão da [documentação oficial do FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/).

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./banco_nsn.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

- **engine:** a conexão com o banco
- **SessionLocal:** cria uma sessão para cada requisição
- **Base:** classe base de onde saem as tabelas
- **get_db():** abre uma sessão e garante que ela seja fechada ao final

> Para trocar para PostgreSQL, basta alterar a `SQLALCHEMY_DATABASE_URL`.

## Tabela `produto`

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | Integer | chave primária, gerada pelo banco |
| `nome` | String | nome do produto |
| `descricao` | String | descrição do produto |
| `preco` | Float | preço |
| `disponivel` | Boolean | se está disponível para venda |

## Equivalência com SQL

| Repositório | SQL gerado |
|---|---|
| `listar()` | `SELECT * FROM produto;` |
| `obter(id)` | `SELECT * FROM produto WHERE id = ?;` |
| `criar(produto)` | `INSERT INTO produto (...) VALUES (...);` |
| `atualizar(id, produto)` | `UPDATE produto SET ... WHERE id = ?;` |
| `remover(id)` | `DELETE FROM produto WHERE id = ?;` |
