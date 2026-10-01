# 6. Casos de Uso

## Diagrama de Casos de Uso

<svg viewBox="0 0 950 470" xmlns="http://www.w3.org/2000/svg" style="max-width:100%; height:auto;">
  <rect x="180" y="20" width="340" height="420" rx="12" fill="#fafafa" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="350" y="45" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#64748b">NSN — MVP</text>
  <rect x="560" y="20" width="360" height="420" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="740" y="45" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#94a3b8">Backlog (fora do MVP)</text>
  <g stroke="#1e3a8a" stroke-width="2" fill="none">
    <circle cx="60" cy="90" r="12" fill="#ffffff"/>
    <line x1="60" y1="102" x2="60" y2="140"/>
    <line x1="35" y1="118" x2="85" y2="118"/>
    <line x1="60" y1="140" x2="40" y2="170"/>
    <line x1="60" y1="140" x2="80" y2="170"/>
  </g>
  <text x="60" y="188" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">Vendedor</text>
  <g stroke="#166534" stroke-width="2" fill="none">
    <circle cx="60" cy="290" r="12" fill="#ffffff"/>
    <line x1="60" y1="302" x2="60" y2="340"/>
    <line x1="35" y1="318" x2="85" y2="318"/>
    <line x1="60" y1="340" x2="40" y2="370"/>
    <line x1="60" y1="340" x2="80" y2="370"/>
  </g>
  <text x="60" y="388" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#166534">Comprador</text>
  <ellipse cx="360" cy="120" rx="140" ry="28" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="124" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC02 Anunciar produto</text>
  <ellipse cx="360" cy="230" rx="140" ry="28" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="234" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC03 Gerenciar anúncio</text>
  <ellipse cx="360" cy="340" rx="140" ry="28" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="344" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e3a8a">UC04 Consultar catálogo</text>
  <ellipse cx="740" cy="80" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="84" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC01 Cadastrar-se</text>
  <ellipse cx="740" cy="125" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="129" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC05 Fazer pedido</text>
  <ellipse cx="740" cy="170" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="174" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC06 Aceitar pedido</text>
  <ellipse cx="740" cy="215" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="219" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC07 Acompanhar pedido</text>
  <ellipse cx="740" cy="260" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="264" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC08 Consultar minhas vendas</text>
  <ellipse cx="740" cy="305" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="309" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC09 Consultar minhas compras</text>
  <ellipse cx="740" cy="350" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="354" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC10 Falar com o vendedor</text>
  <ellipse cx="740" cy="395" rx="150" ry="20" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="740" y="399" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">UC11 Adicionar fotos</text>
  <line x1="90" y1="115" x2="222" y2="120" stroke="#1e3a8a" stroke-width="1.5"/>
  <line x1="90" y1="125" x2="222" y2="226" stroke="#1e3a8a" stroke-width="1.5"/>
  <line x1="90" y1="315" x2="222" y2="340" stroke="#166534" stroke-width="1.5"/>
  <line x1="520" y1="230" x2="560" y2="230" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,3"/>
</svg>

**Legenda:** 🔵 azul = casos de uso do MVP · ⬜ cinza tracejado = backlog, não implementado · linha azul = Vendedor · linha verde = Comprador

Associações de ator para os itens de backlog foram omitidas do diagrama para não
sobrecarregar a leitura visual. Estão detalhadas nos casos de uso abaixo e na seção
[7.7](/requisitos/lista-de-itens-de-trabalho.md).

## UC01 — Cadastrar-se *(backlog)*

> Requisitos relacionados: [RF01](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor ou Comprador |
| **Pré-condição** | Nenhuma |
| **Pós-condição** | Pessoa cadastrada e apta a anunciar e fazer pedidos |

**Fluxo principal**

1. A pessoa informa seu nome e telefone WhatsApp.
2. O sistema valida os dados.
3. O sistema confirma o cadastro.

**Fluxo alternativo A1 — dados incompletos**

- 2a. Se faltar o nome ou o telefone, o sistema avisa e não conclui o cadastro.

---

## UC02 — Anunciar produto

> Requisitos relacionados: [RF02](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor |
| **Pré-condição** | Nenhuma no MVP (no futuro: estar cadastrado) |
| **Pós-condição** | Produto aparece no catálogo |

**Fluxo principal**

1. O vendedor informa nome, descrição, preço e se o produto está disponível.
2. O sistema valida as informações.
3. O sistema salva o produto e o inclui no catálogo.
4. O sistema confirma o anúncio.

**Fluxo alternativo A1 — informação obrigatória faltando**

- 2a. Se faltar nome, descrição ou preço, o sistema recusa o anúncio e informa o
  problema. Nada é salvo.

---

## UC03 — Gerenciar anúncio

> Requisitos relacionados: [RF03, RF04, RF05](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor |
| **Pré-condição** | Produto já anunciado |
| **Pós-condição** | Catálogo reflete os dados atuais do produto |

**Fluxo principal — editar**

1. O vendedor escolhe um produto anunciado.
2. O vendedor altera preço, descrição ou disponibilidade (ex.: marca como esgotado).
3. O sistema valida e salva as alterações.
4. O catálogo passa a mostrar os dados novos.

**Fluxo alternativo A1 — remover anúncio**

- 2a. O vendedor escolhe remover o produto.
- 2b. O sistema retira o produto do catálogo.

**Fluxo alternativo A2 — produto não existe mais**

- 1a. Se o produto já tiver sido removido, o sistema informa que ele não foi
  encontrado.

---

## UC04 — Consultar catálogo

> Requisitos relacionados: [RF06, RF07](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Comprador |
| **Pré-condição** | Nenhuma |
| **Pós-condição** | Comprador vê os produtos anunciados |

**Fluxo principal**

1. O comprador abre o catálogo.
2. O sistema mostra os produtos anunciados, com preço e disponibilidade.
3. O comprador escolhe um produto para ver os detalhes.

**Fluxo alternativo A1 — catálogo vazio**

- 2a. Se não houver produtos anunciados, o sistema mostra o catálogo vazio.

---

## UC05 — Fazer pedido *(backlog)*

> Requisitos relacionados: [RF08](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Comprador |
| **Pré-condição** | Estar cadastrado; produto disponível |
| **Pós-condição** | Pedido registrado com status **Feito** |

**Fluxo principal**

1. O comprador escolhe um produto no catálogo.
2. Informa quantidade, se é entrega ou retirada, o local de entrega e observações
   (sabor, horário, troco).
3. Confirma o pedido.
4. O sistema registra o pedido com status **Feito** e o envia ao vendedor.

**Fluxo alternativo A1 — produto indisponível**

- 1a. Se o produto estiver marcado como indisponível, o sistema não permite o pedido.

---

## UC06 — Aceitar pedido *(backlog)*

> Requisitos relacionados: [RF09, RF10](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Vendedor |
| **Pré-condição** | Existir pedido com status **Feito** para um produto do vendedor |
| **Pós-condição** | Pedido com status **Aceito** |

**Fluxo principal**

1. O vendedor abre seus pedidos recebidos.
2. Escolhe um pedido e o aceita.
3. O sistema muda o status para **Aceito**.

---

## UC07 — Acompanhar pedido *(backlog)*

> Requisitos relacionados: [RF12](/requisitos/requisitos-funcionais.md)

| | |
|---|---|
| **Ator** | Comprador |
| **Pré-condição** | Ter feito ao menos um pedido |
| **Pós-condição** | Comprador sabe o status atual do pedido |

**Fluxo principal**

1. O comprador abre seus pedidos.
2. O sistema mostra o status de cada um (Feito ou Aceito).

---

## Demais casos de uso do backlog

| ID | Caso de uso | Ator | Requisitos |
|---|---|---|---|
| UC08 | Consultar minhas vendas | Vendedor | RF09 |
| UC09 | Consultar minhas compras | Comprador | RF11 |
| UC10 | Falar com o vendedor pelo WhatsApp | Comprador | RF13 |
| UC11 | Adicionar fotos ao produto | Vendedor | RF14 |

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do diagrama e dos casos de uso | Nayra |
| 2026-10-01 | 1.1 | Casos de uso reescritos do ponto de vista do usuário, sem detalhes técnicos | Nayra |
