from flask_openapi3 import APIBlueprint, Tag

from model import Session
from model.categoria import Categoria
from schemas import ListagemCategoriasSchema, apresenta_categorias, ErrorSchema

categoria_tag = Tag(name="Categoria", description="Listagem de categorias de pedais")

categorias_bp = APIBlueprint('categorias', __name__)


@categorias_bp.get('/categorias', tags=[categoria_tag],
                   responses={"200": ListagemCategoriasSchema})
def get_categorias():
    """Lista todas as categorias de pedais disponíveis no sistema."""
    session = Session()
    categorias = session.query(Categoria).all()
    session.close()
    return apresenta_categorias(categorias), 200
