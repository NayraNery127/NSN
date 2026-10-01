# 8. Visão de Arquitetura

## Fluxo geral

<svg viewBox="0 0 900 280" xmlns="http://www.w3.org/2000/svg" style="max-width:100%; height:auto;">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#475569"/>
    </marker>
  </defs>
  <rect x="20" y="110" width="120" height="60" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="80" y="137" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1e3a8a">Cliente</text>
  <text x="80" y="154" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#3b82f6">Postman / Swagger</text>

  <rect x="200" y="110" width="130" height="60" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="265" y="137" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1e3a8a">Rota</text>
  <text x="265" y="154" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#3b82f6">server.py</text>

  <rect x="200" y="20" width="130" height="50" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="265" y="42" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#166534">Schema</text>
  <text x="265" y="58" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#16a34a">Pydantic</text>

  <rect x="390" y="110" width="150" height="60" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="465" y="137" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1e3a8a">Repositório</text>
  <text x="465" y="154" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#3b82f6">acesso aos dados</text>

  <rect x="390" y="210" width="150" height="50" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="465" y="232" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#166534">Model</text>
  <text x="465" y="248" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#16a34a">SQLAlchemy</text>

  <rect x="610" y="110" width="160" height="60" rx="10" fill="#fef3f2" stroke="#e11d48" stroke-width="2"/>
  <text x="690" y="137" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#9f1239">SQLite</text>
  <text x="690" y="154" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#e11d48">banco_nsn.db</text>

  <line x1="140" y1="140" x2="198" y2="140" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="265" y1="70" x2="265" y2="108" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
  <line x1="330" y1="140" x2="388" y2="140" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="465" y1="208" x2="465" y2="172" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
  <line x1="540" y1="140" x2="608" y2="140" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>

  <text x="169" y="130" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#64748b">requisição</text>
  <text x="300" y="92" font-family="sans-serif" font-size="10" fill="#64748b">valida</text>
  <text x="359" y="130" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#64748b">chama</text>
  <text x="480" y="195" font-family="sans-serif" font-size="10" fill="#64748b">usa</text>
  <text x="574" y="130" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#64748b">lê / grava</text>
</svg>

**Legenda:** 🔵 azul = camadas que processam a requisição · 🟢 verde = definições de formato dos dados · 🔴 vermelho = banco de dados

## Camadas

| Camada | Tecnologia | Arquivo | Justificativa |
|---|---|---|---|
| Rota | FastAPI | `src/server.py` | recebe a requisição e chama o repositório |
| Schema | Pydantic | `src/schema/schemas.py` | valida tudo que entra e sai da API, retornando 422 automaticamente |
| Repositório | SQLAlchemy | `src/infra/sqlalchemy/repositorios/produto.py` | única camada que acessa o banco (CRUD) |
| Model | SQLAlchemy | `src/infra/sqlalchemy/models/models.py` | define as tabelas do banco |
| Configuração | SQLAlchemy | `src/infra/sqlalchemy/config/database.py` | conexão com o banco e sessão por requisição |
| Banco | SQLite | `banco_nsn.db` | banco em arquivo, sem instalação |
| Servidor | Uvicorn | — | executa a API localmente |

## Estrutura de pastas

```text
src/
├── server.py
├── schema/
│   └── schemas.py
└── infra/sqlalchemy/
    ├── config/database.py
    ├── models/models.py
    └── repositorios/produto.py
```

## Decisões de projeto

- **Schema separado do model**: o schema define o que a API aceita e devolve; o model
  define como o dado fica guardado. Assim, o formato da API pode mudar sem mexer no
  banco, e vice-versa.
- **Padrão repositório**: as rotas nunca acessam o banco diretamente. Para adicionar
  uma nova operação, basta criar o método no repositório e a rota que o chama.
- **SQLite em vez de PostgreSQL**: os requisitos originais do curso previam
  PostgreSQL com Docker. O SQLite foi escolhido para o MVP por não exigir instalação.
  Como o acesso é feito pelo SQLAlchemy, a migração exige apenas trocar a URL de
  conexão ([RNF06](/requisitos/requisitos-nao-funcionais.md)).
- **Sem camada de serviços, por enquanto**: o fluxograma de referência prevê uma
  camada de regras de negócio entre a rota e o repositório. Como o CRUD de produtos
  não tem regras próprias, ela entra junto com o módulo de pedidos (RN04–RN06).
- **Sessão por requisição (`get_db`)**: cada requisição abre uma sessão com o banco e
  a fecha ao final, mesmo em caso de erro, evitando conexões presas.

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Documentação inicial da arquitetura e decisões de projeto | Nayra |
