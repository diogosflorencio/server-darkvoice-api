from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chaves_validas = {
    "9F4jDs0qLp2ZW1BvH7sRTpM8X": {"status": "active", "usuario": "usuario1"},
    "3G1nQs7eYu5Kl8wZu4R2fJ6Bc": {"status": "active",  "usuario": "usuario2"},
    "X8vF3cH6mZ9Rn4TqS2wJ1dL0p": {"status": "active", "usuario": "usuario3"},
    "P7sM3jA1kL8bV6rT5qN0cW9eY": {"status": "active",  "usuario": "usuario4"},
    "K2vL9rF0sQ8wX4pM6bC3jT1zU": {"status": "active", "usuario": "usuario5"},
    "T5mB8rD0zN2qJ7vF3pX9lC4sK": {"status": "active",  "usuario": "usuario6"},
    "Z1X2C3V4B5N6M7Q8W9E0R1T2Y": {"status": "active", "usuario": "usuario7"},
    "U3I4O5P6L7K8J9H0G1F2D3S4A": {"status": "active",  "usuario": "usuario8"},
    "Q1W2E3R4T5Y6U7I8O9P0A1S2D": {"status": "active", "usuario": "usuario9"},
    "F1G2H3J4K5L6Z7X8C9V0B1N2M": {"status": "active",  "usuario": "usuario10"},
    "P9O8I7U6Y5T4R3E2W1Q0A9S8D": {"status": "active", "usuario": "usuario11"},
    "L0K9J8H7G6F5D4S3A2Z1X0C9V": {"status": "active",  "usuario": "usuario12"},
    "M1N2B3V4C5X6Z7L8K9J0H1G2F": {"status": "active", "usuario": "usuario13"},
    "Q9W8E7R6T5Y4U3I2O1P0A9S8D": {"status": "active",  "usuario": "usuario14"},
    "Z8X7C6V5B4N3M2L1K0J9H8G7F": {"status": "active", "usuario": "usuario15"},
    "A1S2D3F4G5H6J7K8L9Q0W2E3R": {"status": "active",  "usuario": "usuario16"},
    "T9Y8U7I6O5P4L3K2J1H0G9F8D": {"status": "active", "usuario": "usuario17"},
    "S2D3F4G5H6J7K8L9Q0W1E2R3T": {"status": "active",  "usuario": "usuario18"},
    "Z0X9C8V7B6N5M4L3K2J1H0G9F": {"status": "active", "usuario": "usuario19"},
    "P1O2I3U4Y5T6R7E8W9Q0A1S2D": {"status": "active",  "usuario": "usuario20"},
}

@app.post('/')
async def verificar_chave(request: Request):
    try:
        dados = await request.json()
        chave = dados.get('chave')
        if not chave:
            return "invalid"
        if chave not in chaves_validas:
            return "invalid"
        info_chave = chaves_validas[chave]

        if info_chave["status"] == "expired":
            return "expired"

        if info_chave["status"] == "active":
            return chave
    except Exception:
        return "invalid"

if __name__ == "__main__":
    porta = 8000
    uvicorn.run(app, host="0.0.0.0", port=porta)
