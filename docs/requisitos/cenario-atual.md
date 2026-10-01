# 1. Cenário Atual e Negócio

## 1.1. Identificação do Cliente

| | Descrição |
|---|---|
| **Perfil** | Pequenos vendedores autônomos (doces, salgados, marmitas, artesanato) |
| **Canal de venda atual** | WhatsApp, grupos de bairro e redes sociais, com atendimento manual |
| **Volume estimado** | Poucos a dezenas de pedidos por dia, todos por mensagem |
| **Necessidade central** | Um lugar único para anunciar produtos e receber pedidos organizados |

## 1.2. Introdução ao negócio e contexto

Quem vende produtos caseiros normalmente divulga fotos e preços em grupos e status do
WhatsApp, e recebe os pedidos por mensagem: *"Ainda tem bolo de chocolate?"*,
*"Quanto custa o cento de brigadeiro?"*, *"Entrega no meu bairro?"*, *"Pode mandar
troco pra 50?"*.

Esse modelo tem três fragilidades recorrentes:

- **Informação espalhada e desatualizada**: produtos, preços e disponibilidade ficam
  soltos em conversas e imagens antigas. O comprador pede algo que já acabou.
- **Pedidos sem padrão**: cada pedido chega de um jeito, e é comum faltar quantidade,
  endereço, sabor, horário de entrega ou troco, gerando várias mensagens de ida e volta.
- **Falta de acompanhamento**: o comprador não sabe se o pedido foi visto ou aceito, e
  o vendedor não tem uma lista organizada do que vendeu e do que precisa entregar.

## 1.3. Identificação do problema

O problema central identificado é que **anúncios e pedidos de pequenos vendedores
dependem de troca manual de mensagens, sem um catálogo atualizado, sem formato padrão
de pedido e sem confirmação de que o pedido foi aceito**.

Causas associadas:

- Ausência de um catálogo único, com preço e disponibilidade sempre atualizados
- Nenhum formato padrão para os dados de um pedido
- Nenhum registro do status do pedido (feito, aceito)
- Nenhum histórico organizado de vendas e compras

## 1.4. Desafios do projeto

- **Desafio de confiança**: o comprador precisa saber que o pedido chegou e foi
  aceito, sem precisar mandar mensagem perguntando. Ver
  [RN05 e RN06](/requisitos/lista-de-itens-de-trabalho.md).
- **Desafio de padronização**: o pedido precisa reunir, de uma vez, tudo que o
  vendedor precisa saber (quantidade, entrega ou retirada, local, observações). Ver
  [RF08](/requisitos/requisitos-funcionais.md).
- **Desafio de simplicidade**: fazer um pedido precisa ser mais rápido do que mandar
  mensagem, senão o comprador volta para o WhatsApp. Ver
  [RNF01](/requisitos/requisitos-nao-funcionais.md).

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do documento, estruturação do cenário atual e problema | Nayra |
| 2026-10-01 | 1.1 | Desafios reescritos com foco no produto | Nayra |
