# 7. Lista de Itens de Trabalho

## 7.1. Regras de Negócio

| ID | Nome da Regra de Negócio | Descrição |
|---|---|---|
| RN01 | Anúncio aberto | Qualquer pessoa pode anunciar produtos |
| RN02 | Pedido aberto | Qualquer pessoa pode fazer pedidos dos produtos anunciados |
| RN03 | Dados do produto | Todo produto tem nome, descrição, preço e disponibilidade (sim/não) |
| RN04 | Produto indisponível | Produto marcado como indisponível não pode receber pedidos |
| RN05 | Aceite do vendedor | Todo pedido precisa ser aceito pelo vendedor do produto |
| RN06 | Status do pedido | Um pedido começa como **Feito** e passa a **Aceito** quando o vendedor aceita |
| RN07 | Dados do pedido | Todo pedido tem produto, comprador, quantidade, entrega ou retirada e local de entrega |
| RN08 | Quantidade mínima | A quantidade de um pedido deve ser de pelo menos 1 unidade |

## 7.2. Critérios de Valor

Cada item foi avaliado contra 4 critérios (V = atende, -- = não atende):

| Critério | Descrição |
|---|---|
| C1 | Resolve diretamente o problema central (anúncios e pedidos espalhados no WhatsApp) |
| C2 | Reduz erro humano ou informação desatualizada |
| C3 | É pré-requisito para outra funcionalidade do sistema |
| C4 | Melhora diretamente a experiência do comprador |

## 7.3. Justificativa de Valor Atribuído

| ID | Nome | C1 | C2 | C3 | C4 | VF (critérios atendidos) |
|---|---|---|---|---|---|---|
| UC01 | Cadastrar-se | -- | V | V | -- | 2 |
| UC02 | Anunciar produto | V | -- | V | V | 3 |
| UC03 | Gerenciar anúncio | V | V | -- | V | 3 |
| UC04 | Consultar catálogo | V | -- | V | V | 3 |
| UC05 | Fazer pedido | V | V | V | V | 4 |
| UC06 | Aceitar pedido | V | V | -- | V | 3 |
| UC07 | Acompanhar pedido | -- | -- | -- | V | 1 |
| UC08 | Consultar minhas vendas | -- | V | -- | -- | 1 |
| UC09 | Consultar minhas compras | -- | -- | -- | V | 1 |
| UC10 | Falar com o vendedor | -- | -- | -- | V | 1 |
| UC11 | Adicionar fotos | -- | -- | -- | V | 1 |

## 7.4. Cálculo de Prioridade

```text
Peso = VF (critérios atendidos) mapeado em escala de 0 a 10
Valor Final = Peso - CT (Complexidade Técnica)
```

| ID | Nome | VF | Peso | CT | Valor Final (Peso-CT) | MoSCoW | Quadrante | MVP |
|---|---|---|---|---|---|---|---|---|
| UC01 | Cadastrar-se | 2 | 6 | 3 | 3 | Should Have | Quadrante 2 | -- |
| UC02 | Anunciar produto | 3 | 8 | 1 | 7 | Must Have | Quadrante 1 | X |
| UC03 | Gerenciar anúncio | 3 | 8 | 2 | 6 | Must Have | Quadrante 1 | X |
| UC04 | Consultar catálogo | 3 | 8 | 1 | 7 | Must Have | Quadrante 1 | X |
| UC05 | Fazer pedido | 4 | 10 | 4 | 6 | Must Have (próxima versão) | Quadrante 2 | -- |
| UC06 | Aceitar pedido | 3 | 8 | 3 | 5 | Should Have | Quadrante 2 | -- |
| UC07 | Acompanhar pedido | 1 | 3 | 2 | 1 | Could Have | Quadrante 3 | -- |
| UC08 | Consultar minhas vendas | 1 | 3 | 2 | 1 | Could Have | Quadrante 3 | -- |
| UC09 | Consultar minhas compras | 1 | 3 | 2 | 1 | Could Have | Quadrante 3 | -- |
| UC10 | Falar com o vendedor | 1 | 3 | 1 | 2 | Could Have | Quadrante 3 | -- |
| UC11 | Adicionar fotos | 1 | 3 | 4 | -1 | Won't Have (por agora) | Quadrante 4 | -- |

**Nota sobre consistência:** o fluxo de pedidos (UC01, UC05, UC06) tem alto valor, mas
também alta complexidade e **depende do catálogo estar pronto**. Por isso o MVP entrega
primeiro o Quadrante 1 (catálogo), e o Quadrante 2 forma a próxima versão. A pontuação
é um apoio à decisão, não um substituto dela.

## 7.5. Definição dos Quadrantes

| Quadrante | Característica |
|---|---|
| Quadrante 1 | Alto valor e baixa complexidade |
| Quadrante 2 | Alto valor e alta complexidade |
| Quadrante 3 | Baixo valor e baixa complexidade |
| Quadrante 4 | Baixo valor e alta complexidade |

## 7.6. Matriz de Esforço

<table style="width:100%; border-collapse:collapse; text-align:center; table-layout:fixed;">
  <tr>
    <td style="border:1px solid #cbd5e1; padding:8px;"></td>
    <td style="border:1px solid #cbd5e1; padding:8px; font-weight:bold;">Baixa Complexidade</td>
    <td style="border:1px solid #cbd5e1; padding:8px; font-weight:bold;">Alta Complexidade</td>
  </tr>
  <tr>
    <td style="border:1px solid #cbd5e1; padding:8px; font-weight:bold;">Alto Valor</td>
    <td style="border:2px solid #16a34a; background:#dcfce7; padding:12px;">
      <strong>Quadrante 1</strong><br>UC02 · Anunciar produto<br>UC03 · Gerenciar anúncio<br>UC04 · Consultar catálogo
    </td>
    <td style="border:2px solid #2563eb; background:#dbeafe; padding:12px;">
      <strong>Quadrante 2</strong><br>UC01 · Cadastrar-se<br>UC05 · Fazer pedido<br>UC06 · Aceitar pedido
    </td>
  </tr>
  <tr>
    <td style="border:1px solid #cbd5e1; padding:8px; font-weight:bold;">Baixo Valor</td>
    <td style="border:2px solid #ca8a04; background:#fef9c3; padding:12px;">
      <strong>Quadrante 3</strong><br>UC07 · Acompanhar pedido<br>UC08 · Minhas vendas<br>UC09 · Minhas compras<br>UC10 · Falar com o vendedor
    </td>
    <td style="border:2px solid #dc2626; background:#fecaca; padding:12px;">
      <strong>Quadrante 4</strong><br>UC11 · Adicionar fotos
    </td>
  </tr>
</table>

**Legenda:** verde = fazer primeiro (MVP) · azul = próxima versão · amarelo = bom ter · vermelho = evitar por agora

O Quadrante 1 forma o **MVP**. Os demais são os itens listados como fora do MVP em
[3. MVP e Escopo](/requisitos/mvp.md).

## 7.7. Rastreabilidade RF-UC-RNF-RN

| ID | Nome | ID UC | Objetivo UC | RNFs Relacionados | RNs Relacionadas |
|---|---|---|---|---|---|
| RF01 | Cadastrar pessoa | UC01 | Identificar quem vende e quem compra | RNF02, RNF03, RNF04 | RN01, RN02 |
| RF02 | Anunciar produto | UC02 | Incluir produto no catálogo | RNF02, RNF03 | RN01, RN03 |
| RF03 | Editar produto | UC03 | Manter os dados do produto corretos | RNF02, RNF03 | RN03 |
| RF04 | Marcar disponibilidade | UC03 | Evitar pedido de produto esgotado | RNF02 | RN04 |
| RF05 | Remover produto | UC03 | Retirar produto do catálogo | RNF02 | RN03 |
| RF06 | Exibir catálogo | UC04 | Mostrar os produtos anunciados | RNF05, RNF06 | RN03 |
| RF07 | Ver detalhes | UC04 | Mostrar um produto específico | RNF05, RNF06 | RN03 |
| RF08 | Fazer pedido | UC05 | Registrar pedido padronizado | RNF01, RNF02, RNF03 | RN02, RN04, RN07, RN08 |
| RF09 | Ver pedidos recebidos | UC06, UC08 | Organizar as vendas do vendedor | RNF02, RNF04 | RN05 |
| RF10 | Aceitar pedido | UC06 | Confirmar o pedido ao comprador | RNF02 | RN05, RN06 |
| RF11 | Ver pedidos feitos | UC09 | Organizar as compras do comprador | RNF02 | RN06 |
| RF12 | Acompanhar status | UC07 | Informar se o pedido foi aceito | RNF02 | RN06 |
| RF13 | Contato pelo WhatsApp | UC10 | Tirar dúvidas direto com o vendedor | RNF04 | — |
| RF14 | Fotos do produto | UC11 | Mostrar como o produto é | RNF05 | RN03 |

Todas as linhas têm **RNF07 (manutenibilidade)** implicitamente, porque ela se aplica
a toda a base de código, sem exceção.

---

Ver também: [4. Requisitos Funcionais](/requisitos/requisitos-funcionais.md),
[5. Requisitos Não-Funcionais](/requisitos/requisitos-nao-funcionais.md) e
[6. Casos de Uso](/requisitos/casos-de-uso.md).

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação das regras de negócio, priorização, matriz de esforço e rastreabilidade | Nayra |
| 2026-10-01 | 1.1 | Itens reorganizados com foco no produto; novas regras RN07 e RN08 | Nayra |
