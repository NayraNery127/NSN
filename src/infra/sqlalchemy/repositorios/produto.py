from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            disponivel=produto.disponivel,
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        return self.db.query(models.Produto).all()

    def obter(self, id: int):
        return self.db.query(models.Produto).filter(models.Produto.id == id).first()

    def remover(self, id: int):
        produto = self.obter(id)
        if produto:
            self.db.delete(produto)
            self.db.commit()
        return produto

    def atualizar(self, id: int, produto: schemas.Produto):
        db_produto = self.obter(id)
        if db_produto:
            db_produto.nome = produto.nome
            db_produto.descricao = produto.descricao
            db_produto.preco = produto.preco
            db_produto.disponivel = produto.disponivel
            self.db.commit()
        return db_produto