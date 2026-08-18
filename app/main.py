from fastapi import FastAPI
from app.api.router import v1_router
from app.core.config import settings

app = FastAPI()

app.include_router(prefix="/api", router=v1_router)


@app.get("/")
def root():
    return "FastAPI is working!"
