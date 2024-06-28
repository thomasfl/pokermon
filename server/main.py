from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.routers import user, game 

app = FastAPI()

### CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Routers
app.include_router(user.router)
app.include_router(game.router)

### Hello world
@app.get("/")
async def start_page():
    return {"swagger": "http://127.0.0.1:8000/docs"}

### Handler
handler = Mangum(app)
