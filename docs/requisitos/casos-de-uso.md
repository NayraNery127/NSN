# 6. Casos de Uso

## Diagrama de Casos de Uso

<svg viewBox="0 0 950 460" xmlns="http://www.w3.org/2000/svg" style="max-width:100%; height:auto;">
  <rect x="180" y="20" width="340" height="400" rx="12" fill="#fafafa" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="350" y="45" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#64748b">NSN — MVP</text>
  <rect x="560" y="20" width="360" height="400" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="740" y="45" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#94a3b8">Backlog (fora do MVP)</text>
  <g stroke="#1e3a8a" stroke-width="2" fill="none">
    <circle cx="60" cy="100" r="12" fill="#ffffff"/>
    <line x1="60" y1="112" x2="60" y2="150"/>
    <line x1="35" y1="128" x2="85" y2="128"/>
    <line x1="60" y1="150" x2="40" y2="180"/>
    <line x1="60" y1="150" x2="80" y2="180"/>
  </g>
  <text x="60" y="198" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">Vendedor</text>
  <g stroke="#166534" stroke-width="2" fill="none">
    <circle cx="60" cy="280" r="12" fill="#ffffff"/>
    <line x1="60" y1="292" x2="60" y2="330"/>
    <line x1="35" y1="308" x2="85" y2="308"/>
    <line x1="60" y1="330" x2="40" y2="360"/>
    <line x1="60" y1="330" x2="80" y2="360"/>
  </g>
  <text x="60" y="378" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#166534">Comprador</text>
  <ellipse cx="360" cy="90" rx="140" ry="26" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="94" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC01 Anunciar produto</text>
  <ellipse cx="360" cy="160" rx="140" ry="26" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="164" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC02 Listar produtos</text>
  <ellipse cx="360" cy="230" rx="140" ry="26" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="234" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC03 Buscar produto</text>
  <ellipse cx="360" cy="300" rx="140" ry="26" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="304" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC04 Atualizar produto</text>
  <ellipse cx="360" cy="370" rx="140" ry="26" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="374" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC05 Remover produto</text>
  <ellipse cx="740" cy="85" rx="150" ry="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="89" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC06 Cadastrar usuário</text>
  <ellipse cx="740" cy="140" rx="150" ry="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="144" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC07 Fazer pedido</text>
  <ellipse cx="740" cy="195" rx="150" ry="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="199" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC08 Aceitar pedido</text>
  <ellipse cx="740" cy="250" rx="150" ry="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="254" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC09 Acompanhar status</text>
  <ellipse cx="740" cy="305" rx="150" ry="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="309" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC10 Minhas vendas e compras</text>
  <ellipse cx="740" cy="360" rx="150" ry="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="364" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC11 Adicionar fotos</text>
  <line x1="90" y1="120" x2="222" y2="92" stroke="#475569" stroke-width="1.5"/>
  <line x1="90" y1="130" x2="222" y2="298" stroke="#475569" stroke-width="1.5"/>
  <line x1="90" y1="135" x2="222" y2="368" stroke="#475569" stroke-width="1.5"/>
  <line x1="90" y1="300" x2="222" y2="162" stroke="#166534" stroke-width="1.5"/>
  <line x1="90" y1="305" x2="222" y2="232" stroke="#166534" stroke-width="1.5"/>
  <line x1="520" y1="230" x2="560" y2="230" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,3"/>
</svg>

**Legenda:** 🔵 azul = casos de uso do MVP (implementados) · ⬜ cinza tracejado = backlog, não implementado · linhas azuis = Vendedor · linhas verdes = Comprador

Associações de ator para os itens de backlog seguem o mesmo padrão e foram omitidas
do diagrama para não sobrecarregar a leitura visual. Estão detalhadas na tabela da
seção [7.7](/requisitos/lista-de-itens-de-trabalho.md).

## UC01 — Anunciar produto

> Requisitos relacionados: [RF01, RF07](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor |
| **Pré-condição** | Nenhuma |
| **Pós-condição** | Produto persistido no banco, com id gerado automaticamente |

**Fluxo principal**

1. O vendedor envia nome, descrição, preço e disponibilidade (`POST /produtos`).
2. O schema valida os dados recebidos.
3. O repositório salva o produto no banco.
4. O sistema retorna o produto criado, com o id (HTTP 201).

**Fluxo alternativo A1 — dados inválidos**

- 2a. Se faltar um campo obrigatório ou o tipo estiver errado, o sistema recusa o
  pedido (HTTP 422) e nada é salvo.

---

## UC02 — Listar produtos

> Requisitos relacionados: [RF02](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Comprador |
| **Pré-condição** | Nenhuma |
| **Pós-condição** | Lista de produtos exibida (vazia, se não houver produtos) |

**Fluxo principal**

1. O comprador solicita a lista de produtos (`GET /produtos`).
2. O repositório busca todos os produtos no banco.
3. O sistema retorna a lista (HTTP 200).

---

## UC03 — Buscar produto

> Requisitos relacionados: [RF03, RF06](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Comprador |
| **Pré-condição** | Conhecer o id do produto |
| **Pós-condição** | Produto exibido, ou aviso de que não existe |

**Fluxo principal**

1. O comprador informa o id (`GET /produtos/{id}`).
2. O repositório busca o produto no banco.
3. O sistema retorna o produto (HTTP 200).

**Fluxo alternativo A1 — produto inexistente**

- 2a. Se não existir produto com esse id, o sistema retorna HTTP 404.

---

## UC04 — Atualizar produto

> Requisitos relacionados: [RF04, RF06, RF07](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor |
| **Pré-condição** | Produto já cadastrado |
| **Pós-condição** | Dados do produto atualizados no banco |

**Fluxo principal**

1. O vendedor informa o id e os novos dados (`PUT /produtos/{id}`).
2. O schema valida os novos dados.
3. O repositório localiza o produto e substitui os campos.
4. O sistema retorna o produto atualizado (HTTP 200).

**Fluxo alternativo A1 — produto inexistente**

- 3a. Se não existir produto com esse id, o sistema retorna HTTP 404.

**Fluxo alternativo A2 — dados inválidos**

- 2a. O sistema recusa o pedido (HTTP 422) e o produto não é alterado.

---

## UC05 — Remover produto

> Requisitos relacionados: [RF05, RF06](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor |
| **Pré-condição** | Produto já cadastrado |
| **Pós-condição** | Produto removido do banco |

**Fluxo principal**

1. O vendedor informa o id (`DELETE /produtos/{id}`).
2. O repositório localiza e remove o produto.
3. O sistema confirma a remoção (HTTP 200).

**Fluxo alternativo A1 — produto inexistente**

- 2a. O sistema retorna HTTP 404.

---

## Backlog (não implementado)

| ID | Caso de uso | Ator | Requisitos |
|---|---|---|---|
| UC06 | Cadastrar usuário (nome e telefone WhatsApp) | Vendedor / Comprador | RF08 |
| UC07 | Fazer pedido (produto, quantidade, local, entrega ou retirada, observações) | Comprador | RF09 |
| UC08 | Aceitar pedido | Vendedor | RF10 |
| UC09 | Acompanhar status do pedido (Feito, Aceito) | Comprador | RF11 |
| UC10 | Consultar minhas vendas e minhas compras | Vendedor / Comprador | RF12 |
| UC11 | Adicionar fotos ao produto | Vendedor | RF13 |

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do diagrama e dos casos de uso do MVP e do backlog | Nayra |
