from pydantic import BaseModel
from typing import Optional, List

from model.pedal import Pedal


class PedalSchema(BaseModel):
    """Define como um novo pedal a ser cadastrado deve ser representado."""
    nome: str = "Tube Screamer"
    descricao: str = "Overdrive clássico de circuito valvulado"
    categoria_id: int = 1
    imagem: Optional[str] = None


class PedalBuscaSchema(BaseModel):
    """Define o filtro opcional para busca de pedais por categoria."""
    categoria_id: Optional[int] = None

class PedalAtualizaSchema(BaseModel):
    """Define como um pedal a ser atualizado deve ser representado."""
    id: Optional[int] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    categoria_id: Optional[int] = None
    imagem: Optional[str] = None

class PedalPathSchema(BaseModel):
    """Define como um pedal será consultado pela API."""
    id: int

class PedalViewSchema(BaseModel):
    """Define como um pedal será retornado pela API."""
    id: int = 1
    nome: str = "Tube Screamer"
    descricao: str = "Overdrive clássico de circuito valvulado"
    imagem: Optional[str] = None
    categoria_id: int = 1
    categoria_nome: str = "Overdrive"
    data_criacao: str = "2024-01-01T00:00:00"


class ListagemPedaisSchema(BaseModel):
    """Define como a listagem de pedais será retornada."""
    pedais: List[PedalViewSchema]


class PedalDelSchema(BaseModel):
    """Define a estrutura retornada após remoção de um pedal."""
    id: int
    message: str
    nome: str


def apresenta_pedal(pedal: Pedal):
    """Retorna a representação de um único pedal."""
    return {
        "id": pedal.id,
        "nome": pedal.nome,
        "descricao": pedal.descricao,
        "imagem": pedal.imagem,
        "categoria_id": pedal.categoria_id,
        "categoria_nome": pedal.categoria.nome if pedal.categoria else None,
        "data_criacao": pedal.data_criacao.isoformat() if pedal.data_criacao else None,
    }


def apresenta_pedais(pedais: List[Pedal]):
    """Retorna a representação de uma lista de pedais."""
    result = []
    for pedal in pedais:
        result.append(apresenta_pedal(pedal))
    return {"pedais": result}
