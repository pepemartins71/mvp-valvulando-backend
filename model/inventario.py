from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import Union

from model.base import Base


class Inventario(Base):
    __tablename__ = 'inventario'

    id: Mapped[int] = mapped_column(primary_key=True)
    pedal_id: Mapped[int] = mapped_column(ForeignKey("pedal.id"), unique=True, nullable=False)
    data_adicao: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    pedal = relationship("Pedal", back_populates="inventario")

    def __init__(self, pedal_id: int, data_adicao: Union[datetime, None] = None):
        """
        Cria um item de Inventário.

        Arguments:
            pedal_id: id do pedal adicionado ao inventário.
            data_adicao: data de adição (opcional, usa datetime.now por padrão).
        """
        self.pedal_id = pedal_id

        if data_adicao:
            self.data_adicao = data_adicao
