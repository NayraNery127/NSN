from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schema.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_bd()
app = FastAPI()


# LISTAR todos
@app.get('/produtos', response_model=List[Produto])
def listar(db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    return repositorio.listar()


# BUSCAR um
@app.get('/produtos/{id}', response_model=Produto)
def buscar(id: int, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    produto = repositorio.obter(id)
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto


# CRIAR
@app.post('/produtos', status_code=201, response_model=Produto)
def criar(produto: Produto, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    return repositorio.criar(produto)


# ATUALIZAR
@app.put('/produtos/{id}', response_model=Produto)
def atualizar(id: int, produto: Produto, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    produto_novo = repositorio.atualizar(id, produto)
    if produto_novo is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto_novo


# APAGAR
@app.delete('/produtos/{id}')
def apagar(id: int, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    produto = repositorio.remover(id)
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return {'msg': 'Produto apagado'}