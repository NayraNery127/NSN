# NSN

API REST de anúncios e pedidos de produtos — projeto pessoal de back-end em Python,
documentado com o mesmo rigor de Engenharia de Requisitos aplicado em projetos
acadêmicos.

## Contexto do NSN

Pequenos vendedores, como quem vende doces, salgados ou artesanato, costumam divulgar
seus produtos e receber pedidos por mensagens no WhatsApp. Produtos, preços e pedidos
ficam espalhados em conversas, sem padrão e sem controle.

O NSN propõe uma plataforma em que **qualquer pessoa pode anunciar produtos** e
**qualquer pessoa pode fazer pedidos** dos produtos anunciados. Esta primeira versão
entrega o módulo de **produtos**: um CRUD completo, com dados persistidos em banco e
código organizado em camadas.

## Como navegar

- **Requisitos** — cenário atual, stakeholders, escopo do MVP, requisitos funcionais e
  não-funcionais, casos de uso e priorização
- **Arquitetura** — camadas, banco de dados e rotas da API
- **Acompanhamento** — lições aprendidas, cronograma, evidências de funcionamento,
  fontes do código e referências

## Metodologia e inspiração

Os requisitos originais e a organização em camadas vêm do curso **TDS Backend 2021.1
(App BLX)**, adaptados para o NSN. A configuração do banco segue a
[documentação oficial do FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/).
A estrutura desta documentação segue o mesmo padrão do projeto
[Agenda Clínica](https://nayranery127.github.io/Agenda-clinica/). As fontes de cada
parte do código estão registradas em [14. Fontes do Código](/acompanhamento/fontes-do-codigo.md).

## Repositório e execução

Código-fonte completo:
[github.com/NayraNery127/NSN](https://github.com/NayraNery127/NSN)

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install fastapi uvicorn sqlalchemy
uvicorn src.server:app --reload
```

Depois, acesse a documentação interativa em `http://127.0.0.1:8000/docs`.
