# 3. MVP e Escopo

## O que está no MVP

- [UC01](/requisitos/casos-de-uso.md) — Anunciar produto, com nome, descrição, preço e disponibilidade
- [UC02](/requisitos/casos-de-uso.md) — Listar produtos anunciados
- [UC03](/requisitos/casos-de-uso.md) — Buscar um produto pelo id
- [UC04](/requisitos/casos-de-uso.md) — Atualizar um produto
- [UC05](/requisitos/casos-de-uso.md) — Remover um produto
- Validação automática dos dados recebidos — parte de UC01/UC04
- Persistência em banco de dados — parte de todos os casos de uso

## O que está fora do MVP (não implementado de propósito)

- [UC06](/requisitos/casos-de-uso.md) — Cadastro de usuário (nome e telefone WhatsApp)
- [UC07](/requisitos/casos-de-uso.md) — Fazer pedido de um produto anunciado
- [UC08](/requisitos/casos-de-uso.md) — Aceitar pedido (vendedor)
- [UC09](/requisitos/casos-de-uso.md) — Acompanhar status do pedido (Feito, Aceito)
- [UC10](/requisitos/casos-de-uso.md) — Consultar minhas vendas e minhas compras
- [UC11](/requisitos/casos-de-uso.md) — Adicionar fotos aos produtos

Esses itens ficaram de fora conscientemente para manter o MVP focado na base de todo
o sistema: **não existe pedido sem produto**. O módulo de produtos precisava estar
completo, persistido e testado antes de expandir para usuários e pedidos.

## Critério de sucesso do MVP

O MVP é considerado funcional quando, sem perda de dados entre reinícios do servidor,
é possível:

1. Cadastrar um produto e receber o id gerado pelo banco
2. Listar, buscar, atualizar e remover esse produto
3. Receber erro claro ao enviar dados inválidos (422) ou buscar um produto inexistente (404)

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Definição inicial do escopo do MVP | Nayra |
