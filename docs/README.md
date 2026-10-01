# NSN — API de Produtos

API REST para cadastro de produtos, construída em **Python** com **FastAPI** e banco de dados **SQLite**.

O projeto implementa um **CRUD completo** (criar, listar, buscar, atualizar e remover) com os dados **persistidos** em banco, organizado em camadas.

## Tecnologias

| Tecnologia | Função |
|---|---|
| **Python** | linguagem |
| **FastAPI** | framework da API |
| **Uvicorn** | servidor que roda a API |
| **Pydantic** | validação dos dados |
| **SQLAlchemy** | comunicação com o banco (ORM) |
| **SQLite** | banco de dados em arquivo |
| **Postman** | testes das rotas |

## Resumo

- 5 rotas cobrindo o CRUD de produtos
- Dados salvos em banco, não se perdem ao reiniciar o servidor
- Validação automática: dados inválidos retornam erro **422**
- Produto inexistente retorna erro **404**
- Documentação interativa automática em `/docs`

## Próximos passos

- Camada de serviços com regras de negócio (ex: preço não pode ser negativo)
- Entidades de Usuário e Pedido
- Autenticação
- Testes automatizados
- Deploy com PostgreSQL
