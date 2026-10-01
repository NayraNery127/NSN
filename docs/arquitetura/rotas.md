# 10. Rotas da API

URL base local: `http://127.0.0.1:8000` · Documentação interativa: `/docs`

## 10.1. Resumo das rotas

| Método | Rota | Ação | Sucesso | Erros | Caso de uso |
|---|---|---|---|---|---|
| GET | `/produtos` | lista todos os produtos | 200 | — | [UC02](/requisitos/casos-de-uso.md) |
| GET | `/produtos/{id}` | busca um produto | 200 | 404 | [UC03](/requisitos/casos-de-uso.md) |
| POST | `/produtos` | cadastra um produto | 201 | 422 | [UC01](/requisitos/casos-de-uso.md) |
| PUT | `/produtos/{id}` | atualiza um produto | 200 | 404, 422 | [UC04](/requisitos/casos-de-uso.md) |
| DELETE | `/produtos/{id}` | remove um produto | 200 | 404 | [UC05](/requisitos/casos-de-uso.md) |

## 10.2. Formato do produto

| Campo | Tipo | Obrigatório | Observação |
|---|---|---|---|
| `id` | int | não | gerado pelo banco, não precisa ser enviado |
| `nome` | str | sim | — |
| `descricao` | str | sim | — |
| `preco` | float | sim | — |
| `disponivel` | bool | não | padrão: `false` |

## 10.3. Exemplos

**POST /produtos**

```json
{ "nome": "Pudim", "descricao": "leite condensado", "preco": 15, "disponivel": true }
```

Resposta (201):

```json
{ "id": 3, "nome": "Pudim", "descricao": "leite condensado", "preco": 15.0, "disponivel": true }
```

**PUT /produtos/3**

```json
{ "nome": "Pudim", "descricao": "leite condensado", "preco": 18, "disponivel": false }
```

**GET /produtos/999** (404):

```json
{ "detail": "Produto não encontrado" }
```

## 10.4. Status codes

| Código | Significado | Quando ocorre |
|---|---|---|
| 200 | OK | leitura, atualização ou remoção com sucesso |
| 201 | Created | produto cadastrado |
| 404 | Not Found | id inexistente |
| 422 | Unprocessable Entity | campo faltando ou tipo inválido |

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Documentação das rotas, formato do produto e status codes | Nayra |
