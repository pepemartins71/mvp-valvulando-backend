from pydantic import BaseModel
from typing import List

from model.categoria import Categoria


class CategoriaSchema(BaseModel):
    """Define como uma categoria será representada na resposta."""
    id: int = 1
    nome: str = "Overdrive"


class ListagemCategoriasSchema(BaseModel):
    """Define como a listagem de categorias será retornada."""
    categorias: List[CategoriaSchema]


def apresenta_categorias(categorias: List[Categoria]):
    """Retorna a representação de uma lista de categorias."""
    result = []
    for categoria in categorias:
        result.append({
            "id": categoria.id,
            "nome": categoria.nome,
        })
    return {"categorias": result}
