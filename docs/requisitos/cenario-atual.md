# 1. Cenário Atual e Negócio

## 1.1. Identificação do Cliente

| | Descrição |
|---|---|
| **Perfil** | Pequenos vendedores autônomos (doces, salgados, artesanato) |
| **Canal de venda atual** | WhatsApp e redes sociais, com atendimento manual |
| **Volume estimado** | Poucos a dezenas de pedidos por dia, todos por mensagem |
| **Necessidade central** | Centralizar anúncios e pedidos num sistema padronizado |

## 1.2. Introdução ao negócio e contexto

Quem vende produtos caseiros normalmente divulga fotos e preços em grupos e status do
WhatsApp, e recebe os pedidos por mensagem: *"Ainda tem bolo de chocolate?"*,
*"Quanto custa o cento de brigadeiro?"*, *"Entrega no meu bairro?"*.

Esse modelo tem três fragilidades recorrentes:

- **Informação espalhada**: produtos, preços e disponibilidade ficam soltos em
  conversas e imagens, e mudam sem que o comprador saiba.
- **Pedidos sem padrão**: cada pedido chega de um jeito, e é comum faltar
  quantidade, endereço, sabor, horário ou troco.
- **Falta de acompanhamento**: o comprador não sabe se o pedido foi visto ou aceito,
  e o vendedor não tem uma lista organizada das suas vendas.

## 1.3. Identificação do problema

O problema central identificado é que **anúncios e pedidos dependem de troca manual
de mensagens, sem um registro único, padronizado e persistente dos produtos e dos
pedidos**.

Causas associadas:

- Ausência de um catálogo único de produtos com preço e disponibilidade
- Nenhum formato padrão para os dados de um pedido
- Nenhum registro do status do pedido (feito, aceito)

## 1.4. Desafios do projeto

- **Desafio de persistência**: os dados precisam sobreviver a reinícios do servidor.
  Ver [RNF02](/requisitos/requisitos-nao-funcionais.md).
- **Desafio de validação**: dados incompletos ou inválidos não podem entrar no
  sistema. Ver [RF07](/requisitos/requisitos-funcionais.md) e
  [RNF03](/requisitos/requisitos-nao-funcionais.md).
- **Desafio de evolução**: o código precisa estar organizado para receber usuários e
  pedidos sem reescrever o que já existe. Ver
  [RNF05](/requisitos/requisitos-nao-funcionais.md).

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do documento, estruturação do cenário atual e problema | Nayra |
