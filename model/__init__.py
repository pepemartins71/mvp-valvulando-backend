from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

from model.base import Base
from model.categoria import Categoria
from model.pedal import Pedal
from model.inventario import Inventario

db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = 'sqlite:///%s/valvulando.sqlite3' % db_path
engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)


def seed_data():
    """Popula o banco com categorias, pedais e inventário iniciais, se estiver vazio."""
    session = Session()

    if session.query(Categoria).count() == 0:
        categorias = [
            Categoria('Overdrive'),
            Categoria('Amplificador'),
            Categoria('Delay'),
            Categoria('Reverb'),
        ]
        session.add_all(categorias)
        session.commit()

        overdrive = session.query(Categoria).filter(Categoria.nome == 'Overdrive').first()
        amplificador = session.query(Categoria).filter(Categoria.nome == 'Amplificador').first()
        delay = session.query(Categoria).filter(Categoria.nome == 'Delay').first()
        reverb = session.query(Categoria).filter(Categoria.nome == 'Reverb').first()

        pedais = [
            Pedal('Tube Screamer', 'Overdrive clássico de circuito valvulado', overdrive.id),
            Pedal('JHS', 'Overdrive boutique de alta qualidade', overdrive.id),
            Pedal('Morning Glory', 'Overdrive transparente baseado no Marshall Blues Breaker', overdrive.id),
            Pedal('OCD', 'Overdrive/distortion versátil da Fulltone', overdrive.id),
            Pedal('Klon', 'O overdrive mais lendário do mercado', overdrive.id),
            Pedal('Digital Delay', 'Delay digital com controles simples de tempo e feedback', delay.id),
            Pedal('Digital Echoes', 'Delay digital com emulação de ecos encadeados', delay.id),
            Pedal('Tape Delay', 'Simulação de delay analógico a fita com warmth natural', delay.id),
            Pedal('Strymon El Capistan', 'Delay a fita de alta fidelidade da Strymon', delay.id),
            Pedal('Strymon Timeline', 'Multi-delay com 12 tipos de delay em um único pedal', delay.id),
            Pedal('RV-6', 'Reverb digital compacto e versátil da Boss', reverb.id),
            Pedal('Kailani', 'Reverb boutique com controle de pitch e shimmer', reverb.id),
            Pedal('Shimmer', 'Reverb com efeito shimmer de pitch ascendente', reverb.id),
            Pedal('Strymon BigSky', 'Reverb de referência com 12 algoritmos de alta qualidade', reverb.id),
            Pedal('TC Electronic Hall of Fame', 'Reverb digital versátil com tecnologia TonePrint', reverb.id),
            Pedal('Fender Twin Reverb', 'Amplificador valvulado americano clássico de 85W', amplificador.id),
            Pedal('Vox AC30', 'Amplificador valvulado britânico icônico dos anos 60', amplificador.id),
            Pedal('Mesa Boogie Dual Rectifier', 'Amplificador de alta ganho para rock e metal pesado', amplificador.id),
            Pedal('Matchless DC-30', 'Amplificador valvulado boutique de referência premium', amplificador.id),
            Pedal('Marshall JCM800', 'Amplificador valvulado britânico para rock clássico', amplificador.id),
        ]
        session.add_all(pedais)
        session.commit()

        tube_screamer = session.query(Pedal).filter(Pedal.nome == 'Tube Screamer').first()
        digital_delay = session.query(Pedal).filter(Pedal.nome == 'Digital Delay').first()
        rv6 = session.query(Pedal).filter(Pedal.nome == 'RV-6').first()
        fender = session.query(Pedal).filter(Pedal.nome == 'Fender Twin Reverb').first()

        inventario_inicial = [
            Inventario(tube_screamer.id),
            Inventario(digital_delay.id),
            Inventario(rv6.id),
            Inventario(fender.id),
        ]
        session.add_all(inventario_inicial)
        session.commit()

        print("Banco de dados populado com dados iniciais.")

    session.close()
