from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
import os

RESTDB_TOKEN = "db318ea2b16bffaa2354f5bc8754036550ac8"
url = 'https://tintas-c736.restdb.io/rest/tintas-usadas'
headers = {
    'Content-type': 'application/json',
    'x-apikey': RESTDB_TOKEN
}

def inserir(data):
    r = requests.post(url, json=data, headers=headers)
    return r.json()

def listar():
    r = requests.get(url, headers=headers)
    return r.json()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {'data': listar()}

@app.post('/')
async def adicionar_tinta(request: Request):
    data = await request.json()
    resultado = inserir(data)
    return resultado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
