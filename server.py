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

# Valid keys database
valid_keys = {
    "3utryg*&T&UG#&Rto73gtf7w3tf9473f": {"status": "active", "user": "Cleitin"},
    "twr789t3rf789t387ft87T*(&t8o7wgfuigff": {"status": "expired", "user": "Joao"},
    "iu3tr7wgf78tf873ofr78two87ft8o73tf87wef": {"status": "active", "user": "Ever"},
}

@app.post('/')
async def verify_key(request: Request):
    try:
        data = await request.json()
        key = data.get('key')

        if not key:
            return "invalid"

        if key not in valid_keys:
            return "invalid"

        key_info = valid_keys[key]
        
        if key_info["status"] == "expired":
            return "expirado"
        
        if key_info["status"] == "active":
            return key

    except Exception:
        return "invalid"

if __name__ == "__main__":
    port = 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
