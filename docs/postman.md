# Testes no Postman

Com o servidor rodando, as rotas podem ser testadas no **Postman**.

## Listar produtos

1. Método **GET**
2. URL: `http://127.0.0.1:8000/produtos`
3. **Send** → retorna a lista de produtos

## Cadastrar produto

1. Método **POST**
2. URL: `http://127.0.0.1:8000/produtos`
3. Aba **Body** → **raw** → **JSON**
4. Corpo:

```json
{ "nome": "Pudim", "descricao": "leite condensado", "preco": 15, "disponivel": true }
```

5. **Send** → retorna **201 Created**

## Atualizar produto

1. Método **PUT**
2. URL: `http://127.0.0.1:8000/produtos/3`
3. **Body** → **raw** → **JSON**
4. Corpo:

```json
{ "nome": "Pudim", "descricao": "leite condensado", "preco": 18, "disponivel": false }
```

5. **Send** → retorna **200** com o produto atualizado

## Remover produto

1. Método **DELETE**
2. URL: `http://127.0.0.1:8000/produtos/3`
3. **Send** → retorna `{ "msg": "Produto apagado" }`

## Testando erros

- **404:** buscar um id que não existe, ex: `GET /produtos/999`
- **422:** cadastrar sem o campo `nome`
