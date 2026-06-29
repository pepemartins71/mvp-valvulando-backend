from flask_openapi3 import APIBlueprint, Tag
from sqlalchemy.exc import IntegrityError

from model import Session
from model.pedal import Pedal
from schemas import (PedalSchema, PedalBuscaSchema,
                     ListagemPedaisSchema, PedalViewSchema,
                     apresenta_pedal, apresenta_pedais, ErrorSchema,
                     PedalPathSchema, PedalAtualizaSchema, PedalDelSchema)

pedal_tag = Tag(name="Pedal", description="Gerenciamento do catálogo de pedais")

pedais_bp = APIBlueprint('pedais', __name__)


@pedais_bp.get('/pedais', tags=[pedal_tag],
               responses={"200": ListagemPedaisSchema})
def get_pedais(query: PedalBuscaSchema):
    """Lista todos os pedais do catálogo, com filtro opcional por categoria."""
    session = Session()

    try:
        if query.categoria_id:
            pedais = session.query(Pedal).filter(Pedal.categoria_id == query.categoria_id).all()
        else:
            pedais = session.query(Pedal).all()

        result = apresenta_pedais(pedais)
        session.close()
        return result, 200
    except Exception as e:
        session.close()
        return {"message": str(e)}, 400

@pedais_bp.delete('/pedais/<id>', tags=[pedal_tag],
                responses={"200": PedalDelSchema, "404": ErrorSchema})
def del_pedal(path: PedalPathSchema):
    """Remove um pedal do catálogo do mercado."""
    session = Session()
    try:
        pedal = session.query(Pedal).filter(Pedal.id == path.id).first()
        if pedal is None:
            session.close()
            return {"message": "Pedal não encontrado."}, 404

        session.delete(pedal)
        session.commit()
        session.close()
        return {"id": path.id, "message": "Pedal removido do catálogo com sucesso.", "nome": pedal.nome}, 200

    except Exception as e:
        session.rollback()
        session.close()
        return {"message": str(e)}, 400


@pedais_bp.put('/pedais/<id>', tags=[pedal_tag],
                responses={"200": PedalViewSchema, "409": ErrorSchema, "404": ErrorSchema})
def update_pedal(path: PedalPathSchema, form: PedalAtualizaSchema):
    """Atualiza um pedal no catálogo do mercado."""
    session = Session()
    try:
        pedal = session.query(Pedal).filter(Pedal.id == path.id).first()
        if pedal is None:
            session.close()
            return {"message": "Pedal não encontrado."}, 404

        nome = form.nome
        descricao = form.descricao
        imagem = form.imagem
        categoria_id = form.categoria_id

        if nome is not None:
            pedal.nome = nome
        if descricao is not None:
            pedal.descricao = descricao
        if imagem is not None:
            pedal.imagem = imagem
        if categoria_id is not None:
            pedal.categoria_id = categoria_id

        session.commit()
        result = apresenta_pedal(pedal)
        session.close()
        return result, 200

    except IntegrityError:
        session.rollback()
        session.close()
        return {"message": "Pedal com esse nome já existe no catálogo."}, 409

    except Exception:
        session.rollback()
        session.close()
        return {"message": "Não foi possível cadastrar o pedal."}, 400


@pedais_bp.post('/pedais', tags=[pedal_tag],
                responses={"201": PedalViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pedal(form: PedalSchema):
    """Cadastra um novo pedal no catálogo do mercado."""
    pedal = Pedal(
        nome=form.nome,
        descricao=form.descricao,
        categoria_id=form.categoria_id,
        imagem=form.imagem
    )
    session = Session()
    try:
        session.add(pedal)
        session.commit()
        session.refresh(pedal)
        result = apresenta_pedal(pedal)
        session.close()
        return result, 201

    except IntegrityError:
        session.rollback()
        session.close()
        return {"message": "Pedal com esse nome já existe no catálogo."}, 409

    except Exception:
        session.rollback()
        session.close()
        return {"message": "Não foi possível cadastrar o pedal."}, 400
