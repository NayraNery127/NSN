# 5. Requisitos Não-Funcionais

| ID | Descrição | Categoria |
|---|---|---|
| RNF01 | A aplicação deve ser uma API REST, usando métodos HTTP e status codes padronizados | Interoperabilidade |
| RNF02 | Os dados devem ser persistidos em banco e sobreviver a reinícios do servidor | Confiabilidade |
| RNF03 | Todo dado recebido deve ser validado automaticamente antes de chegar ao banco (Pydantic) | Confiabilidade |
| RNF04 | A API deve gerar documentação interativa automática (Swagger em `/docs`) | Usabilidade |
| RNF05 | O código deve ser organizado em camadas com responsabilidade única (rota, schema, repositório, model) | Manutenibilidade |
| RNF06 | A troca de banco (ex.: SQLite para PostgreSQL) deve exigir apenas a alteração da URL de conexão | Portabilidade |
| RNF07 | O ambiente de desenvolvimento deve ser isolado por projeto (ambiente virtual Python) | Portabilidade |

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Levantamento inicial dos requisitos não-funcionais | Nayra |
