# 14. Fontes do Código

Registro de onde vem a base da camada de dados e do repositório do projeto. Documentar as fontes mostra
o processo real de desenvolvimento e onde cada decisão se apoiou.

> Para adicionar os prints, salve as imagens na pasta `docs/acompanhamento/img/` com
> os nomes indicados em cada seção.

## 14.1. Resumo

| Arquivo | Camada | Fonte | Adaptações feitas |
|---|---|---|---|
| `database.py` | Configuração do banco | [Documentação oficial do FastAPI — SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) | nome do banco, import atualizado do `declarative_base`, funções `criar_bd` e `get_db` no mesmo arquivo |
| `models.py` | Tabelas do banco | [Documentação oficial do FastAPI — SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) | tabela `produto` com os campos do NSN |
| `schemas.py` | Validação dos dados | [Documentação oficial do FastAPI — SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) | schema `Produto` com os campos do NSN e `from_attributes` (Pydantic v2) |
| `produto.py` | Repositório (acesso aos dados) | Padrão Repositório, com base no `crud.py` da [documentação oficial do FastAPI — SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) | funções organizadas numa classe `RepositorioProduto`; método `atualizar` criado para o NSN |

---

## 14.2. `database.py`

**Caminho:** `src/infra/sqlalchemy/config/database.py`
**Função:** faz a conexão com o banco e entrega uma sessão para cada requisição.

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./banco_nsn.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

**Adaptações:** o nome do banco virou `banco_nsn.db`; o `declarative_base` passou a ser
importado de `sqlalchemy.orm`, como pede a versão atual do SQLAlchemy; as funções
`criar_bd()` e `get_db()` ficaram no próprio arquivo de configuração.

**Fonte:**

![Fonte do database.py](img/fonte-database.png)

---

## 14.3. `models.py`

**Caminho:** `src/infra/sqlalchemy/models/models.py`
**Função:** define a tabela `produto` do banco.

```python
class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
```

**Adaptações:** a tabela e os campos foram definidos de acordo com o produto do NSN
(nome, descrição, preço e disponibilidade — [RN03](/requisitos/lista-de-itens-de-trabalho.md)).

**Fonte:**

![Fonte do models.py](img/fonte-models.png)

---

## 14.4. `schemas.py`

**Caminho:** `src/schema/schemas.py`
**Função:** valida os dados que entram e saem da API.

```python
class Produto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    nome: str
    descricao: str
    preco: float
    disponivel: bool = False
```

**Adaptações:** campos iguais aos do model, para as duas camadas conversarem sem
conversões; `from_attributes=True` permite ao Pydantic ler os objetos que vêm do banco.

**Fonte:**

![Fonte do schemas.py](img/fonte-schemas.png)

---

## 14.5. `produto.py` (repositório)

**Caminho:** `src/infra/sqlalchemy/repositorios/produto.py`
**Função:** é a única camada que acessa o banco. Cada método é uma operação do CRUD.

```python
class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto): ...
    def listar(self): ...
    def obter(self, id: int): ...
    def atualizar(self, id: int, produto: schemas.Produto): ...
    def remover(self, id: int): ...
```

| Método | O que faz | Caso de uso |
|---|---|---|
| `criar` | salva um produto novo | [UC02](/requisitos/casos-de-uso.md) |
| `listar` | retorna todos os produtos | [UC04](/requisitos/casos-de-uso.md) |
| `obter` | retorna um produto pelo id | [UC04](/requisitos/casos-de-uso.md) |
| `atualizar` | altera os dados de um produto | [UC03](/requisitos/casos-de-uso.md) |
| `remover` | apaga um produto | [UC03](/requisitos/casos-de-uso.md) |

**Adaptações:** em vez de funções soltas, as operações foram reunidas numa classe que
recebe a sessão do banco uma única vez; o método `atualizar` foi criado para permitir
editar anúncios e marcar produtos como esgotados.

**Fonte:**

![Fonte do repositório](img/fonte-repositorio.png)

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do registro de fontes do código | Nayra |
| 2026-10-01 | 1.1 | Registro focado na camada de dados: database.py, models.py e schemas.py | Nayra |
| 2026-10-01 | 1.2 | Adiciona o repositório (produto.py) | Nayra |
