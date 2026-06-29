from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

from model import seed_data
from routes.categorias import categorias_bp
from routes.pedais import pedais_bp
from routes.inventario import inventario_bp

info = Info(title="Valvulando API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

seed_data()

app.register_api(categorias_bp)
app.register_api(pedais_bp)
app.register_api(inventario_bp)


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para a documentação interativa da API."""
    return redirect('/openapi')


if __name__ == '__main__':
    app.run(debug=True)
