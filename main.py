from fastapi import FastAPI
from json_db import JsonDB
from imdb import generate_products
from product import Product

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_products():
    products = productDB.read()
    return{'Products': products}

@app.post('/products')
def create_product(product: Product):
    productDB.insert(product)
    return{'Products': product}