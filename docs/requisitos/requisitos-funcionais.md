# 4. Requisitos Funcionais

| ID | Descrição | Prioridade |
|---|---|---|
| RF01 | O sistema deve permitir que qualquer pessoa anuncie um produto com nome, descrição, preço e disponibilidade (sim/não) | Alta |
| RF02 | O sistema deve permitir a listagem de todos os produtos anunciados | Alta |
| RF03 | O sistema deve permitir buscar um produto pelo seu id | Alta |
| RF04 | O sistema deve permitir atualizar os dados de um produto | Alta |
| RF05 | O sistema deve permitir remover um produto | Alta |
| RF06 | O sistema deve informar quando um produto não for encontrado (HTTP 404) | Alta |
| RF07 | O sistema deve recusar dados incompletos ou com tipo inválido (HTTP 422) | Alta |
| RF08 | O sistema deve permitir cadastrar pessoas, com nome e telefone WhatsApp | Média |
| RF09 | O sistema deve permitir que qualquer pessoa faça pedidos dos produtos anunciados, informando quantidade, local de entrega, entrega ou retirada e observações (sabor, horário, troco etc.) | Média |
| RF10 | O sistema deve permitir que o vendedor aceite um pedido | Média |
| RF11 | O sistema deve permitir que o comprador acompanhe o status dos seus pedidos (Feito, Aceito) | Média |
| RF12 | O sistema deve manter, para cada usuário, a lista de pedidos recebidos (minhas vendas) e de pedidos feitos (minhas compras) | Baixa |
| RF13 | O sistema deve permitir adicionar fotos aos produtos | Baixa |

## Rastreabilidade

Cada RF está mapeado a um Caso de Uso, além de RNFs e RNs relacionadas. A tabela
completa de rastreabilidade está em
[7. Lista de Itens de Trabalho](/requisitos/lista-de-itens-de-trabalho.md).

RF01–RF05 formam o CRUD de produtos e derivam do problema de informação espalhada
descrito em [1. Cenário Atual e Negócio](/requisitos/cenario-atual.md). RF09–RF11
derivam dos problemas de pedidos sem padrão e falta de acompanhamento.

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Levantamento inicial dos requisitos funcionais a partir dos requisitos do App BLX | Nayra |
