from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class Produto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    nome: str
    descricao: str
    preco: float
    disponivel: bool = False


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    meus_produtos: List[Produto] = []
    minhas_vendas: List['Pedido'] = []
    meus_pedidos: List['Pedido'] = []


class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observacoes'


Usuario.model_rebuild()
