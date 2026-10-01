# 7. Lista de Itens de Trabalho

## 7.1. Regras de Negócio

| ID | Nome da Regra de Negócio | Descrição |
|---|---|---|
| RN01 | Anúncio aberto | Qualquer pessoa pode anunciar produtos |
| RN02 | Pedido aberto | Qualquer pessoa pode fazer pedidos dos produtos anunciados |
| RN03 | Dados do produto | Todo produto tem nome, descrição, preço e disponibilidade (sim/não) |
| RN04 | Produto indisponível | Produto marcado como indisponível não pode receber pedidos |
| RN05 | Aceite do vendedor | Todo pedido precisa ser aceito pelo vendedor |
| RN06 | Status do pedido | Um pedido passa pelos status Feito e Aceito |

## 7.2. Critérios de Valor

Cada item foi avaliado contra 4 critérios (V = atende, -- = não atende):

| Critério | Descrição |
|---|---|
| C1 | Resolve diretamente o problema central (anúncios e pedidos espalhados) |
| C2 | Reduz erro humano ou informação desatualizada |
| C3 | É pré-requisito técnico para outra funcionalidade do sistema |
| C4 | Foi explicitamente solicitado nos requisitos originais (App BLX) |

## 7.3. Justificativa de Valor Atribuído

| ID | Nome | C1 | C2 | C3 | C4 | VF (critérios atendidos) |
|---|---|---|---|---|---|---|
| UC01 | Anunciar produto | V | -- | V | V | 3 |
| UC02 | Listar produtos | V | -- | -- | V | 2 |
| UC03 | Buscar produto | -- | V | V | -- | 2 |
| UC04 | Atualizar produto | V | V | -- | -- | 2 |
| UC05 | Remover produto | V | V | -- | -- | 2 |
| UC06 | Cadastrar usuário | -- | -- | V | V | 2 |
| UC07 | Fazer pedido | V | V | V | V | 4 |
| UC08 | Aceitar pedido | V | V | -- | V | 3 |
| UC09 | Acompanhar status | -- | -- | -- | V | 1 |
| UC10 | Minhas vendas e compras | -- | -- | -- | V | 1 |
| UC11 | Adicionar fotos | -- | -- | -- | -- | 0 |

## 7.4. Cálculo de Prioridade

```text
Peso = VF (critérios atendidos) mapeado em escala de 0 a 10
Valor Final = Peso - CT (Complexidade Técnica)
```

| ID | Nome | VF | Peso | CT | Valor Final (Peso-CT) | MoSCoW | Quadrante | MVP |
|---|---|---|---|---|---|---|---|---|
| UC01 | Anunciar produto | 3 | 8 | 1 | 7 | Must Have | Quadrante 1 | X |
| UC02 | Listar produtos | 2 | 6 | 1 | 5 | Must Have | Quadrante 1 | X |
| UC03 | Buscar produto | 2 | 6 | 1 | 5 | Should Have | Quadrante 1 | X |
| UC04 | Atualizar produto | 2 | 6 | 2 | 4 | Should Have | Quadrante 1 | X |
| UC05 | Remover produto | 2 | 6 | 1 | 5 | Should Have | Quadrante 1 | X |
| UC06 | Cadastrar usuário | 2 | 6 | 3 | 3 | Should Have | Quadrante 2 | -- |
| UC07 | Fazer pedido | 4 | 10 | 4 | 6 | Must Have (próxima versão) | Quadrante 2 | -- |
| UC08 | Aceitar pedido | 3 | 8 | 3 | 5 | Should Have | Quadrante 2 | -- |
| UC09 | Acompanhar status | 1 | 3 | 2 | 1 | Could Have | Quadrante 3 | -- |
| UC10 | Minhas vendas e compras | 1 | 3 | 3 | 0 | Could Have | Quadrante 4 | -- |
| UC11 | Adicionar fotos | 0 | 0 | 4 | -4 | Won't Have (por agora) | Quadrante 4 | -- |

**Nota sobre consistência:** o módulo de pedidos (UC06–UC08) tem alto valor, mas também
alta complexidade e **depende do módulo de produtos** estar pronto. Por isso o MVP
entrega primeiro o Quadrante 1 (produtos), e o Quadrante 2 forma a próxima versão. A
pontuação é um apoio à decisão, não um substituto dela.

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
      <strong>Quadrante 1</strong><br>UC01 · Anunciar produto<br>UC02 · Listar produtos<br>UC03 · Buscar produto<br>UC04 · Atualizar produto<br>UC05 · Remover produto
    </td>
    <td style="border:2px solid #2563eb; background:#dbeafe; padding:12px;">
      <strong>Quadrante 2</strong><br>UC06 · Cadastrar usuário<br>UC07 · Fazer pedido<br>UC08 · Aceitar pedido
    </td>
  </tr>
  <tr>
    <td style="border:1px solid #cbd5e1; padding:8px; font-weight:bold;">Baixo Valor</td>
    <td style="border:2px solid #ca8a04; background:#fef9c3; padding:12px;">
      <strong>Quadrante 3</strong><br>UC09 · Acompanhar status
    </td>
    <td style="border:2px solid #dc2626; background:#fecaca; padding:12px;">
      <strong>Quadrante 4</strong><br>UC10 · Minhas vendas e compras<br>UC11 · Adicionar fotos
    </td>
  </tr>
</table>

**Legenda:** verde = fazer primeiro (MVP) · azul = próxima versão · amarelo = bom ter · vermelho = evitar por agora

O Quadrante 1 forma o **MVP**. Os demais são os itens listados como fora do MVP em
[3. MVP e Escopo](/requisitos/mvp.md).

## 7.7. Rastreabilidade RF-UC-RNF-RN

| ID | Nome | ID UC | Objetivo UC | RNFs Relacionados | RNs Relacionadas |
|---|---|---|---|---|---|
| RF01 | Anunciar produto | UC01 | Cadastrar um produto no catálogo | RNF01, RNF02, RNF03 | RN01, RN03 |
| RF02 | Listar produtos | UC02 | Mostrar todos os produtos anunciados | RNF01, RNF02 | RN03 |
| RF03 | Buscar produto | UC03 | Mostrar um produto específico | RNF01, RNF02 | RN03 |
| RF04 | Atualizar produto | UC04 | Manter preço e disponibilidade corretos | RNF01, RNF02, RNF03 | RN03, RN04 |
| RF05 | Remover produto | UC05 | Retirar produto do catálogo | RNF01, RNF02 | RN03 |
| RF06 | Produto não encontrado | UC03, UC04, UC05 | Informar id inexistente (404) | RNF01 | — |
| RF07 | Recusar dados inválidos | UC01, UC04 | Impedir dados incompletos (422) | RNF03 | RN03 |
| RF08 | Cadastrar pessoa | UC06 | Identificar vendedor e comprador | RNF02, RNF03 | RN01, RN02 |
| RF09 | Fazer pedido | UC07 | Registrar pedido padronizado | RNF02, RNF03 | RN02, RN04 |
| RF10 | Aceitar pedido | UC08 | Confirmar pedido pelo vendedor | RNF02 | RN05, RN06 |
| RF11 | Acompanhar status | UC09 | Mostrar status ao comprador | RNF02 | RN06 |
| RF12 | Minhas vendas e compras | UC10 | Listar pedidos por usuário | RNF02 | RN05 |
| RF13 | Fotos do produto | UC11 | Exibir imagens do produto | RNF02 | RN03 |

Todas as linhas têm **RNF05 (arquitetura em camadas)** implicitamente, porque ela se
aplica a toda a base de código, sem exceção.

---

Ver também: [4. Requisitos Funcionais](/requisitos/requisitos-funcionais.md),
[5. Requisitos Não-Funcionais](/requisitos/requisitos-nao-funcionais.md) e
[6. Casos de Uso](/requisitos/casos-de-uso.md).

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação das regras de negócio, priorização, matriz de esforço e rastreabilidade | Nayra |
