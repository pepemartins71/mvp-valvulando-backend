from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from model.base import Base


class Categoria(Base):
    __tablename__ = 'categoria'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    pedais = relationship("Pedal", back_populates="categoria")

    def __init__(self, nome: str):
        """
        Cria uma Categoria de pedal.

        Arguments:
            nome: nome da categoria (ex: Overdrive, Reverb, Delay, Amplificador).
        """
        self.nome = nome
