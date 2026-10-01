# 11. Lições Aprendidas

Registro honesto dos problemas reais encontrados durante o desenvolvimento — e como
foram resolvidos. O valor aqui está em documentar o processo real, erros incluídos.

## Ambiente e infraestrutura

| Problema | Causa | Solução |
|---|---|---|
| Pacotes instalados no Python global | ambiente virtual criado, mas não ativado | ativar com `venv\Scripts\Activate.ps1` e conferir o `(venv)` no terminal |
| `Activate.ps1` não encontrado | pasta nova, sem ambiente virtual criado | criar antes com `python -m venv venv` |
| `Could not import module` | nome do arquivo diferente do usado no comando | o comando segue o padrão `uvicorn pasta.arquivo:app` (ex.: `src.server:app`) |
| `pip install SQAlchemy` falhou | erro de digitação no nome do pacote | o nome correto é `sqlalchemy` |
| Pasta `src` criada como arquivo | criação pelo botão errado | `mkdir` cria pasta, `New-Item` cria arquivo |

## Código e arquitetura

| Problema | Causa | Solução |
|---|---|---|
| Dados sumiam ao reiniciar o servidor | dados guardados em lista na memória | persistência em banco com SQLAlchemy + SQLite |
| Classe usada antes de existir | `Usuario` referenciava `Produto` e `Pedido` declarados depois | nomes entre aspas + `model_rebuild()` |
| Campos com nomes diferentes entre schema e model | `detalhes` no schema e `descricao` no model | padronizar o mesmo nome nas duas camadas |
| Erro ao devolver dados do banco | Pydantic não lia objetos do SQLAlchemy | `from_attributes=True` no schema |

## Testes da API

| Problema | Causa | Solução |
|---|---|---|
| 422 no POST pelo Swagger | JSON colado embaixo do exemplo, gerando dois JSON juntos | apagar o exemplo antes de colar |
| PUT recusado no Swagger | id da rota não preenchido em *Parameters* | o PUT precisa do id na rota **e** dos dados no corpo |
| 404 na raiz da API | a rota `/` não existia | testar as rotas existentes, como `/produtos` |

## Principal aprendizado

Para adicionar uma nova operação, basta mexer em **duas camadas**: o repositório
(a ação no banco) e a rota (o pedido que chama essa ação). Model e schema só mudam
quando o **formato do dado** muda.

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Registro inicial das lições aprendidas durante o desenvolvimento | Nayra |
