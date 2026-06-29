from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import Optional, Union

from model.base import Base


class Pedal(Base):
    __tablename__ = 'pedal'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(140), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(String(500), nullable=False)
    imagem: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categoria.id"), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    categoria = relationship("Categoria", back_populates="pedais")
    inventario = relationship("Inventario", back_populates="pedal", uselist=False)

    def __init__(self, nome: str, descricao: str, categoria_id: int,
                 imagem: Union[str, None] = None,
                 data_criacao: Union[datetime, None] = None):
        """
        Cria um Pedal.

        Arguments:
            nome: nome do pedal.
            descricao: descrição do pedal.
            categoria_id: id da categoria à qual o pedal pertence.
            imagem: nome do arquivo de imagem (opcional).
            data_criacao: data de inserção (opcional, usa datetime.now por padrão).
        """
        self.nome = nome
        self.descricao = descricao
        self.categoria_id = categoria_id
        self.imagem = imagem

        if data_criacao:
            self.data_criacao = data_criacao
