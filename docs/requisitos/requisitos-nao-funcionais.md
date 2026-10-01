# 5. Requisitos Não-Funcionais

| ID | Descrição | Categoria |
|---|---|---|
| RNF01 | Um pedido deve poder ser feito em até 3 passos (escolher produto, preencher dados, confirmar), para ser mais rápido que uma conversa no WhatsApp | Usabilidade |
| RNF02 | Produtos e pedidos não podem ser perdidos: todos os dados devem ficar salvos de forma permanente | Confiabilidade |
| RNF03 | O sistema deve recusar anúncios e pedidos com informações obrigatórias faltando ou inválidas | Confiabilidade |
| RNF04 | O telefone do comprador só deve ficar visível para o vendedor do pedido, em conformidade com a LGPD | Segurança e Privacidade |
| RNF05 | O catálogo deve carregar em até 2 segundos em condições normais de rede | Desempenho |
| RNF06 | O sistema deve poder ser consumido por qualquer interface (site, aplicativo ou ferramenta de teste), por meio de uma API padronizada | Interoperabilidade |
| RNF07 | O sistema deve estar organizado de forma que novas funcionalidades (usuários, pedidos) possam ser adicionadas sem reescrever as existentes | Manutenibilidade |
| RNF08 | O banco de dados deve poder ser trocado (ex.: de SQLite para PostgreSQL) sem alterar as regras do sistema | Portabilidade |

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Levantamento inicial dos requisitos não-funcionais | Nayra |
| 2026-10-01 | 1.1 | Requisitos reescritos com foco na qualidade do produto | Nayra |
