# Valvulando API

API REST para gerenciamento de pedais de guitarra. O sistema permite organizar um catálogo de pedais do mercado e controlar um inventário pessoal, com suporte a categorias como Overdrive, Delay, Reverb e Amplificador.

## Tecnologias

- Python 3.10+
- Flask
- flask-openapi3 (Swagger/OpenAPI)
- SQLAlchemy (ORM)
- Pydantic (validação de schemas)
- SQLite
- Flask-CORS

## Pré-requisitos

- Python 3.10 ou superior instalado
- pip

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/mvp-valvulando-backend.git
   cd mvp-valvulando-backend
   ```

2. Crie o ambiente virtual:
   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Como executar

Com o ambiente virtual ativo, execute:

```
python app.py
```

O servidor será iniciado em `http://localhost:5000`.

O banco de dados SQLite será criado automaticamente na pasta `database/` e populado com dados iniciais (categorias, pedais e inventário) na primeira execução.

## Documentação da API

Com o servidor rodando, acesse a documentação interativa (Swagger) em:

```
http://localhost:5000/openapi
```

### Rotas disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /categorias | Lista todas as categorias de pedais |
| GET | /pedais | Lista todos os pedais do catálogo (filtro opcional por `categoria_id`) |
| POST | /pedais | Cadastra um novo pedal no catálogo |
| PUT | /pedais/{id} | Atualiza os dados de um pedal existente |
| DELETE | /pedais/{id} | Remove um pedal do catálogo do mercado |
| GET | /inventario | Lista os pedais do inventário pessoal |
| POST | /inventario | Adiciona um pedal ao inventário pessoal |
| DELETE | /inventario/{id} | Remove um pedal do inventário pessoal |