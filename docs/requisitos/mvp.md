# 3. MVP e Escopo

## O que está no MVP

O MVP entrega a base de todo o produto: o **catálogo do vendedor**. Não existe pedido
sem produto, então essa parte precisava estar completa antes de qualquer outra.

- [UC02](/requisitos/casos-de-uso.md) — Anunciar produto, com nome, descrição, preço e disponibilidade
- [UC03](/requisitos/casos-de-uso.md) — Gerenciar anúncio: editar dados, marcar como disponível ou indisponível, remover
- [UC04](/requisitos/casos-de-uso.md) — Consultar catálogo e ver os detalhes de um produto

## O que está fora do MVP (não implementado de propósito)

- [UC01](/requisitos/casos-de-uso.md) — Cadastro de pessoa (nome e telefone WhatsApp)
- [UC05](/requisitos/casos-de-uso.md) — Fazer pedido
- [UC06](/requisitos/casos-de-uso.md) — Aceitar pedido
- [UC07](/requisitos/casos-de-uso.md) — Acompanhar status do pedido
- [UC08](/requisitos/casos-de-uso.md) — Consultar minhas vendas
- [UC09](/requisitos/casos-de-uso.md) — Consultar minhas compras
- [UC10](/requisitos/casos-de-uso.md) — Falar com o vendedor pelo WhatsApp
- [UC11](/requisitos/casos-de-uso.md) — Adicionar fotos ao produto

Esses itens ficaram de fora conscientemente para manter o MVP focado no primeiro
problema do cenário: **informação espalhada e desatualizada**. Com o catálogo pronto,
a próxima versão entrega o fluxo de pedidos.

## Critério de sucesso do MVP

O MVP é considerado funcional quando um vendedor consegue, sem perder nenhuma
informação:

1. Anunciar um produto com preço e disponibilidade
2. Atualizar o preço ou marcar o produto como esgotado
3. Retirar um produto que não vende mais

E um comprador consegue ver o catálogo sempre atualizado.

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Definição inicial do escopo do MVP | Nayra |
| 2026-10-01 | 1.1 | Escopo reescrito com foco no produto (catálogo do vendedor) | Nayra |
