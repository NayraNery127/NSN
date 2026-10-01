# 9. Banco de Dados

## 9.1. Visão geral

| | Descrição |
|---|---|
| **Banco** | SQLite (arquivo `banco_nsn.db`) |
| **ORM** | SQLAlchemy |
| **Criação das tabelas** | automática, na primeira execução (`criar_bd()`) |
| **Configuração** | `src/infra/sqlalchemy/config/database.py` |
| **Fonte da configuração** | [documentação oficial do FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/) |

O SQLAlchemy é um ORM: o código é escrito em Python e ele gera o SQL correspondente,
enviando ao banco e convertendo a resposta de volta para objetos Python.

## 9.2. Componentes da configuração

| Componente | Função |
|---|---|
| `SQLALCHEMY_DATABASE_URL` | endereço do banco (`sqlite:///./banco_nsn.db`) |
| `engine` | conexão com o banco |
| `SessionLocal` | cria uma sessão para cada requisição |
| `Base` | classe base de onde saem as tabelas |
| `criar_bd()` | cria as tabelas a partir dos models |
| `get_db()` | abre a sessão, entrega para a rota e fecha ao final |

## 9.3. Tabela `produto`

| Coluna | Tipo | Restrição | Descrição |
|---|---|---|---|
| `id` | Integer | chave primária, indexada | gerado automaticamente pelo banco |
| `nome` | String | — | nome do produto |
| `descricao` | String | — | detalhamento do produto |
| `preco` | Float | — | preço |
| `disponivel` | Boolean | — | disponível para venda (sim/não) |

## 9.4. Equivalência com SQL

| Método do repositório | SQL gerado | CRUD |
|---|---|---|
| `criar(produto)` | `INSERT INTO produto (...) VALUES (...)` | Create |
| `listar()` | `SELECT * FROM produto` | Read |
| `obter(id)` | `SELECT * FROM produto WHERE id = ?` | Read |
| `atualizar(id, produto)` | `UPDATE produto SET ... WHERE id = ?` | Update |
| `remover(id)` | `DELETE FROM produto WHERE id = ?` | Delete |

## 9.5. Tabelas previstas (backlog)

| Tabela | Campos principais | Caso de uso |
|---|---|---|
| `usuario` | nome, telefone WhatsApp | [UC01](/requisitos/casos-de-uso.md) |
| `pedido` | produto, usuário, quantidade, local de entrega, entrega ou retirada, observações, status | [UC05–UC07](/requisitos/casos-de-uso.md) |

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Documentação do banco, tabela produto e equivalência com SQL | Nayra |
