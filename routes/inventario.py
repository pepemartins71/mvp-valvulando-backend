from flask_openapi3 import APIBlueprint, Tag
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from model import Session
from model.inventario import Inventario
from schemas import (InventarioSchema, InventarioPathSchema, InventarioViewSchema,
                     ListagemInventarioSchema, InventarioDelSchema,
                     apresenta_inventario_item, apresenta_inventario, ErrorSchema)

inventario_tag = Tag(name="Inventário", description="Gerenciamento do inventário pessoal de pedais")

inventario_bp = APIBlueprint('inventario', __name__)

@inventario_bp.get('/inventario', tags=[inventario_tag],
                   responses={"200": ListagemInventarioSchema})
def get_inventario():
    """Lista todos os pedais presentes no inventário pessoal."""
    session = Session()
    try:
        itens = session.query(Inventario).all()
        result = apresenta_inventario(itens)
        session.close()
        return result, 200
    except Exception as e:
        session.close()
        return {"message": str(e)}, 400


@inventario_bp.post('/inventario', tags=[inventario_tag],
                    responses={"201": InventarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_inventario(form: InventarioSchema):
    """Adiciona um pedal do catálogo ao inventário pessoal."""
    session = Session()
    try:
        item = Inventario(pedal_id=form.pedal_id)
        session.add(item)
        session.commit()
        session.refresh(item)
        result = apresenta_inventario_item(item)
        session.close()
        return result, 201

    except IntegrityError:
        session.rollback()
        session.close()
        return {"message": "Esse pedal já está no seu inventário."}, 409

    except Exception:
        session.rollback()
        session.close()
        return {"message": "Não foi possível adicionar ao inventário."}, 400


@inventario_bp.delete('/inventario/<id>', tags=[inventario_tag],
                      responses={"200": InventarioDelSchema, "404": ErrorSchema})
def del_inventario(path: InventarioPathSchema):
    """Remove um pedal do inventário pessoal pelo id do item."""
    session = Session()
    item = session.query(Inventario).filter(Inventario.id == path.id).first()

    if not item:
        session.close()
        return {"message": "Item não encontrado no inventário."}, 404

    try:
        session.delete(item)
        session.commit()
        session.close()
        return {"message": "Pedal removido do inventário com sucesso.", "id": path.id}, 200
    except Exception as e:
        session.rollback()
        session.close()
        return {"message": str(e)}, 400
