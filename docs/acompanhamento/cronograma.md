# 12. Cronograma e Entregas

Linha do tempo das fases do projeto, do estudo inicial até a publicação da
documentação.

| Fase | Data | O que foi entregue |
|---|---|---|
| 1. Fundamentos | 29/09/2026 | Estudo de FastAPI: rotas, métodos HTTP, status codes, Pydantic e testes no Postman |
| 2. Estrutura | 30/09/2026 | Criação das pastas em camadas, ambiente virtual e schemas (Produto, Usuário, Pedido) |
| 3. Banco de dados | 30/09/2026 | Configuração do SQLAlchemy com SQLite, model da tabela `produto` |
| 4. Repositório e rotas | 30/09/2026 | CRUD de produtos (criar, listar, buscar, remover) persistido em banco |
| 5. Atualização | 30/09/2026 | Rota PUT e método `atualizar` no repositório |
| 6. Testes | 01/10/2026 | Testes de todas as rotas no Swagger e no Postman |
| 7. Engenharia de Requisitos | 01/10/2026 | Cenário, stakeholders, MVP, RFs, RNFs, casos de uso e priorização |
| 8. Publicação | 01/10/2026 | Site de documentação publicado via GitHub Pages |

## Próximas entregas

| Fase | O que será entregue |
|---|---|
| 9. Usuários | Cadastro de pessoas ([UC01](/requisitos/casos-de-uso.md)) |
| 10. Pedidos | Fazer pedido, aceite e status ([UC05–UC07](/requisitos/casos-de-uso.md)) |
| 11. Serviços | Camada de regras de negócio (RN04–RN08) |
| 12. Infraestrutura | Migração para PostgreSQL com Docker |

## Observação sobre a ordem

Assim como no Agenda Clínica, a documentação de requisitos (fase 7) veio **depois**
da implementação (fases 2–6), o inverso da ordem ideal. Isso é reconhecido
intencionalmente: o objetivo foi aplicar o raciocínio de requisitos ao produto como um
todo, incluindo o que ainda será construído.

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do cronograma de fases do projeto | Nayra |
