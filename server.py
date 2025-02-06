from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Novo objeto JSON contendo nome de usuário e chave
usuarios = {
    "usuario1": {"nome": "Cleitin", "key": "3utryg*&T&UG#&Rto73gtf7w3tf973f"},
    "usuario2": {"nome": "Joao", "key": "twr789t3rf789t387ft87T*(&t8o7wgfuigff"},
    "usuario3": {"nome": "Ever", "key": "iu3tr7wgf78tf873ofr78two87ft8o73tf87wef"},
}

@app.get('/')
def home():
    # Retorna os dados do JSON com nome e chave dos usuários
    return {"usuarios": usuarios}

@app.post('/')
async def adicionar_usuario(request: Request):
    # Recebe um JSON e faz algo com ele
    data = await request.json()
    # Por exemplo, apenas envia de volta os dados recebidos (a lógica pode ser expandida conforme necessário)
    return {"received_data": data}

if __name__ == "__main__":
    port = 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
