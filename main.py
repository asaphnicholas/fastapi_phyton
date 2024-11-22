
from fastapi import FastAPI

app = FastAPI()


vendas = {
    1: {"item": "lata", "preco_unitario": 4, "qualidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 4, "qualidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 4, "qualidade": 5},
    4: {"item": "lata mini", "preco_unitario": 4, "qualidade": 5},
}

@app.get("/")

def home():
    return {"Vendas": len(vendas)}


@app.get("/Vendas/{id_vendas}")

def pegar_venda(id_venda: int):
        return vendas[id_venda]

# # Define uma rota (endpoint)
# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# # Outro exemplo de endpoint com parâmetro
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}