# Como rodar

## Pré-requisitos

- Python 3 instalado
- Git

## Passo a passo

**1. Clonar o repositório**

```bash
git clone https://github.com/NayraNery127/NSN.git
cd NSN
```

**2. Criar e ativar o ambiente virtual**

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**3. Instalar as dependências**

```bash
pip install fastapi uvicorn sqlalchemy
```

**4. Rodar o servidor**

```bash
uvicorn src.server:app --reload
```

**5. Acessar**

- API: http://127.0.0.1:8000
- Documentação interativa (Swagger): http://127.0.0.1:8000/docs

O arquivo `banco_nsn.db` é criado automaticamente na primeira execução.
