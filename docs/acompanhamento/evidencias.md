# 13. Evidências de Software

Capturas de tela da API funcionando, como prova de que os requisitos documentados
foram efetivamente implementados.

> Para adicionar os prints, salve as imagens na pasta `docs/acompanhamento/img/`
> com os nomes indicados abaixo.

## Documentação interativa com todas as rotas

Swagger gerado automaticamente pelo FastAPI ([RNF06](/requisitos/requisitos-nao-funcionais.md)),
com as cinco rotas do CRUD de produtos.

![Swagger](img/swagger-rotas.png)

## Listagem de produtos (GET)

Resposta real da API no Postman (`GET /produtos`), confirmando que os produtos
cadastrados permanecem salvos no banco entre reinícios do servidor.

![GET listar](img/postman-get-listar.png)

## Cadastro de produto (POST)

Cadastro do produto "Pudim" no Postman, com retorno **201 Created** e id gerado pelo
banco.

![POST criar](img/postman-post-criar.png)

## Atualização de produto (PUT)

Atualização do produto 1 (Bolo) de chocolate para morango e de 25,50 para 30,00, com
retorno **200**.

![PUT atualizar](img/put-atualizar.png)

## Produtos persistidos no banco de dados

Tabela `produto` aberta no SQLite Viewer, confirmando que os dados estão gravados no
arquivo `banco_nsn.db`.

![Banco de dados](img/banco-de-dados.png)

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Estrutura das evidências de funcionamento da API | Nayra |
