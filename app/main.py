from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import v1_router
from app.core.config import settings
from alembic import command
from alembic.config import Config

is_development = settings.ENVIRONMENT == "development"

allowed_origins = (
    ["http://localhost:5173", "http://localhost:4173"] if is_development else []
)


@asynccontextmanager
async def startup_event():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    yield


app = FastAPI(
    title="Mayan Task Management API",
    docs_url="/docs" if is_development else None,
    redoc_url="/redoc" if is_development else None,
    openapi_url="/openapi.json" if is_development else None,
    debug=is_development,
)

app.include_router(prefix="/api", router=v1_router)

app.frontend("/", directory="dist", fallback="index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
