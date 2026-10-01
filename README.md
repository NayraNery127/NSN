# NSN — API de Produtos

API REST para cadastro de produtos, construída em Python com FastAPI e banco de dados SQLite.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Estrutura

- `server.py`: rotas da API
- `schema/schemas.py`: validação dos dados
- `config/database.py`: conexão com o banco
- `models/models.py`: tabelas do banco
- `repositorios/produto.py`: acesso ao banco (CRUD)

## Rotas

- `GET /produtos`: lista todos
- `GET /produtos/{id}`: busca um
- `POST /produtos`: cadastra
- `PUT /produtos/{id}`: atualiza
- `DELETE /produtos/{id}`: remove

## Como rodar

    pip install fastapi uvicorn sqlalchemy
    uvicorn src.server:app --reload

Acesse http://127.0.0.1:8000/docs para testar.
