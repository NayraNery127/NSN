# 14. Fontes do Código

Registro de onde cada parte do código e da documentação foi tirada ou adaptada.
Documentar as fontes é tão importante quanto o código: mostra o processo real de
aprendizado e onde cada decisão se apoiou.

> Para adicionar os prints, salve as imagens na pasta `docs/acompanhamento/img/`
> com os nomes indicados abaixo.

## 14.1. Resumo das fontes

| Parte do projeto | Arquivo | Fonte | Adaptações feitas |
|---|---|---|---|
| Requisitos do sistema | [Requisitos](/requisitos/requisitos-funcionais.md) | Curso TDS Backend 2021.1 (App BLX) | organizados em RFs, RNFs, casos de uso e priorização |
| Estrutura de pastas | `src/` | Curso TDS Backend 2021.1 (App BLX) | pastas `router`, `services` e `utils` ainda não utilizadas |
| Fluxograma da arquitetura | [8. Visão Geral](/arquitetura/README.md) | Curso TDS Backend 2021.1 (App BLX) | camada de serviços adiada para o módulo de pedidos |
| Configuração do banco | `database.py` | [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/) | nome do banco, import atualizado do `declarative_base`, funções `criar_bd` e `get_db` |
| Model de produto | `models.py` | Curso TDS Backend 2021.1 (App BLX) | — |
| Repositório | `produto.py` | Curso TDS Backend 2021.1 (App BLX), completado com auxílio de IA | método `atualizar` adicionado |
| Rotas | `server.py` | Curso TDS Backend 2021.1 (App BLX), completado com auxílio de IA | rota PUT e tratamento de 404 |
| Estrutura da documentação | `docs/` | Projeto [Agenda Clínica](https://nayranery127.github.io/Agenda-clinica/) | adaptada para o NSN |

## 14.2. Requisitos originais (App BLX)

Funcionalidades, atributos de pessoa, produto e pedido, e ferramentas previstas no
curso.

![Requisitos BLX](img/fonte-requisitos-blx.png)

## 14.3. Estrutura de pastas

![Estrutura do projeto](img/fonte-estrutura-pastas.png)

## 14.4. Fluxograma da arquitetura

![Fluxograma](img/fonte-fluxograma.png)

## 14.5. Configuração do banco (documentação do FastAPI)

![Documentação FastAPI](img/fonte-documentacao-fastapi.png)

## 14.6. Model de produto

![Model](img/fonte-model.png)

## 14.7. Repositório

![Repositório](img/fonte-repositorio.png)

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do registro de fontes do código | Nayra |
