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
            Pedal('Tube Screamer', 'Overdrive clássico de circuito valvulado', overdrive.id, 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Ibanez_ts9_tube_screamer.jpg'),
            Pedal('JHS', 'Overdrive boutique de alta qualidade', overdrive.id, 'https://cdn.shopify.com/s/files/1/0610/7122/9028/files/JHSPedalsKiltV2.png?v=1698431980'),
            Pedal('Morning Glory', 'Overdrive transparente baseado no Marshall Blues Breaker', overdrive.id, 'https://cdn.shopify.com/s/files/1/0610/7122/9028/files/MG-Clean.png?v=1769698894'),
            Pedal('OCD', 'Overdrive/distortion versátil da Fulltone', overdrive.id, 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Fulltone_OCD_v.1.jpg'),
            Pedal('Klon', 'O overdrive mais lendário do mercado', overdrive.id, 'https://upload.wikimedia.org/wikipedia/commons/f/f7/Klon_Centaur.jpg'),
            Pedal('Digital Delay', 'Delay digital com controles simples de tempo e feedback', delay.id, 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Boss_DD-7_Digital_Delay.jpg'),
            Pedal('Digital Echoes', 'Delay digital com emulação de ecos encadeados', delay.id, 'https://upload.wikimedia.org/wikipedia/commons/3/39/Boss_DD-5_Digital_Delay.jpg'),
            Pedal('Tape Delay', 'Simulação de delay analógico a fita com warmth natural', delay.id, 'https://upload.wikimedia.org/wikipedia/commons/1/10/Danelectro_Reel_Echo.jpg'),
            Pedal('Strymon El Capistan', 'Delay a fita de alta fidelidade da Strymon', delay.id, 'https://upload.wikimedia.org/wikipedia/commons/5/57/Strymon_El_Capistan_8455.jpg'),
            Pedal('Strymon Timeline', 'Multi-delay com 12 tipos de delay em um único pedal', delay.id, 'https://www.strymon.net/wp-content/uploads/2021/03/timeline_topdown_grad_1600.jpeg'),
            Pedal('RV-6', 'Reverb digital compacto e versátil da Boss', reverb.id, 'https://static.roland.com/products/rv-6/image/rv-6_hero.jpg'),
            Pedal('Kailani', 'Reverb boutique com controle de pitch e shimmer', reverb.id, 'https://gearhero.com/cdn/shop/products/31b728b6-5352-49e6-8b2b-79c070bd0ae3.jpg?v=1706803005'),
            Pedal('Shimmer', 'Reverb com efeito shimmer de pitch ascendente', reverb.id, 'https://cdn-media.empowertribe.com/1335701f975d41358efd5aa08275fc2b/Image_TE_0709-AHS_FLUORESCENCE-SHIMMER-REVERB_Left_B.png'),
            Pedal('Strymon BigSky', 'Reverb de referência com 12 algoritmos de alta qualidade', reverb.id, 'https://upload.wikimedia.org/wikipedia/commons/9/99/Strymon_BigSky_DSCF3842.jpg'),
            Pedal('TC Electronic Hall of Fame', 'Reverb digital versátil com tecnologia TonePrint', reverb.id, 'https://cdn.long-mcquade.com/files/89214/lg_001bf7f4f1d5468573b0b7d880e7a715.jpg'),
            Pedal('Fender Twin Reverb', 'Amplificador valvulado americano clássico de 85W', amplificador.id, 'https://upload.wikimedia.org/wikipedia/commons/c/ce/FenderTwin.jpg'),
            Pedal('Vox AC30', 'Amplificador valvulado britânico icônico dos anos 60', amplificador.id, 'https://upload.wikimedia.org/wikipedia/commons/5/56/VOX_AC30_Twin.jpg'),
            Pedal('Mesa Boogie Dual Rectifier', 'Amplificador de alta ganho para rock e metal pesado', amplificador.id, 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Mesa_Boogie_Dual_Rectifier_Tremoverb_100w_Head.jpg'),
            Pedal('Matchless DC-30', 'Amplificador valvulado boutique de referência premium', amplificador.id, 'https://cdn.prod.website-files.com/5e4f4ddcf45e4c7d053435f5/5e5c14060e1706c543840f3b_C-30Reverb.jpeg'),
            Pedal('Marshall JCM800', 'Amplificador valvulado britânico para rock clássico', amplificador.id, 'https://upload.wikimedia.org/wikipedia/commons/4/4f/Marshall_JCM800_amplifier.jpg'),
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
