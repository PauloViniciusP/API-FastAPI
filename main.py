from fastapi import FastAPI
from imdb import generate_products

app = FastAPI()

products = generate_products()

@app.get('/')
def get_products():
    return{'Products': products}