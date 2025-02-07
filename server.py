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
    "aaa1": {"status": "active", "user": "Cleitin"},
    "aaa0": {"status": "expired", "user": "Joao"},
    "bbb1": {"status": "active", "user": "Ever"},
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
