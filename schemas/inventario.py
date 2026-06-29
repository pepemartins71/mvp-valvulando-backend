from pydantic import BaseModel
from typing import Optional, List

from model.inventario import Inventario


class InventarioPathSchema(BaseModel):
    """Path parameter para identificar um item do inventário pelo id."""
    id: int


class InventarioSchema(BaseModel):
    """Define como um item a ser adicionado ao inventário deve ser representado."""
    pedal_id: int = 1


class InventarioViewSchema(BaseModel):
    """Define como um item do inventário será retornado pela API."""
    id: int = 1
    pedal_id: int = 1
    pedal_nome: str = "Tube Screamer"
    pedal_descricao: str = "Overdrive clássico"
    pedal_imagem: Optional[str] = None
    categoria_nome: str = "Overdrive"
    data_adicao: str = "2024-01-01T00:00:00"


class ListagemInventarioSchema(BaseModel):
    """Define como a listagem do inventário será retornada."""
    inventario: List[InventarioViewSchema]


class InventarioDelSchema(BaseModel):
    """Define a estrutura retornada após remoção de um item do inventário."""
    message: str
    id: int


def apresenta_inventario_item(item: Inventario):
    """Retorna a representação de um único item do inventário."""
    return {
        "id": item.id,
        "pedal_id": item.pedal_id,
        "pedal_nome": item.pedal.nome if item.pedal else None,
        "pedal_descricao": item.pedal.descricao if item.pedal else None,
        "pedal_imagem": item.pedal.imagem if item.pedal else None,
        "categoria_nome": item.pedal.categoria.nome if item.pedal and item.pedal.categoria else None,
        "data_adicao": item.data_adicao.isoformat() if item.data_adicao else None,
    }


def apresenta_inventario(itens: List[Inventario]):
    """Retorna a representação de uma lista de itens do inventário."""
    result = []
    for item in itens:
        result.append(apresenta_inventario_item(item))
    return {"inventario": result}
