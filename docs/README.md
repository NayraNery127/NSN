# NSN

Plataforma de anúncios e pedidos para pequenos vendedores — projeto pessoal de
back-end em Python, documentado com o mesmo rigor de Engenharia de Requisitos
aplicado em projetos acadêmicos.

## Contexto do NSN

Quem vende doces, salgados ou artesanato costuma divulgar os produtos e receber
pedidos por mensagens no WhatsApp. Produtos, preços e pedidos ficam espalhados em
conversas, sem padrão e sem controle: o comprador não sabe o que está disponível, e o
vendedor perde pedidos no meio das mensagens.

O NSN propõe um lugar único onde **qualquer pessoa pode anunciar produtos** e
**qualquer pessoa pode fazer pedidos**, com pedidos padronizados, aceite pelo
vendedor e acompanhamento de status pelo comprador.

## Como navegar

- **Requisitos** — cenário atual, stakeholders, escopo do MVP, requisitos funcionais e
  não-funcionais, casos de uso e priorização
- **Arquitetura** — camadas, banco de dados e rotas da API
- **Acompanhamento** — lições aprendidas, cronograma, evidências de funcionamento,
  fontes do código e referências

## Metodologia e inspiração

A estrutura de documentação de requisitos (cenário atual, stakeholders, MVP,
RFs/RNFs, casos de uso e priorização) segue o mesmo padrão aplicado no projeto
[Agenda Clínica](https://nayranery127.github.io/Agenda-clinica/). A configuração da
camada de dados segue a
[documentação oficial do FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/).

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
