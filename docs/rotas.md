# Rotas da API

URL base: `http://127.0.0.1:8000`

| Método | Rota | Ação | Sucesso |
|---|---|---|---|
| <span class="metodo get">GET</span> | `/produtos` | lista todos os produtos | 200 |
| <span class="metodo get">GET</span> | `/produtos/{id}` | busca um produto | 200 |
| <span class="metodo post">POST</span> | `/produtos` | cadastra um produto | 201 |
| <span class="metodo put">PUT</span> | `/produtos/{id}` | atualiza um produto | 200 |
| <span class="metodo delete">DELETE</span> | `/produtos/{id}` | remove um produto | 200 |

---

## <span class="metodo get">GET</span> Listar produtos

`GET /produtos`

**Resposta 200**

```json
[
  { "id": 1, "nome": "Bolo", "descricao": "morango", "preco": 30.0, "disponivel": true },
  { "id": 2, "nome": "Brigadeiro", "descricao": "chocolate", "preco": 3.0, "disponivel": true }
]
```

---

## <span class="metodo get">GET</span> Buscar produto

`GET /produtos/{id}`

**Resposta 200**

```json
{ "id": 1, "nome": "Bolo", "descricao": "morango", "preco": 30.0, "disponivel": true }
```

**Resposta 404**

```json
{ "detail": "Produto não encontrado" }
```

---

## <span class="metodo post">POST</span> Cadastrar produto

`POST /produtos`

**Corpo da requisição**

```json
{ "nome": "Pudim", "descricao": "leite condensado", "preco": 15, "disponivel": true }
```

> O `id` não precisa ser enviado: o banco gera automaticamente.

**Resposta 201**

```json
{ "id": 3, "nome": "Pudim", "descricao": "leite condensado", "preco": 15.0, "disponivel": true }
```

**Resposta 422:** algum campo obrigatório faltando ou com tipo errado.

---

## <span class="metodo put">PUT</span> Atualizar produto

`PUT /produtos/{id}`

**Corpo da requisição**

```json
{ "nome": "Pudim", "descricao": "leite condensado", "preco": 18, "disponivel": false }
```

**Resposta 200**

```json
{ "id": 3, "nome": "Pudim", "descricao": "leite condensado", "preco": 18.0, "disponivel": false }
```

**Resposta 404:** produto não encontrado.

---

## <span class="metodo delete">DELETE</span> Remover produto

`DELETE /produtos/{id}`

**Resposta 200**

```json
{ "msg": "Produto apagado" }
```

**Resposta 404:** produto não encontrado.

---

## Status codes

| Código | Significado |
|---|---|
| **200** | sucesso |
| **201** | criado com sucesso |
| **404** | produto não encontrado |
| **422** | dados inválidos |
