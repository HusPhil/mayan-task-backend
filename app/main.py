from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import v1_router
from app.core.config import settings

is_development = settings.ENVIRONMENT == "development"

allowed_origins = (
    ["http://localhost:5173", "http://localhost:4173"] if is_development else []
)

app = FastAPI(
    title="Mayan Task Management API",
    docs_url="/docs" if is_development else None,
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

# if is_development:

#     @app.get("/")
#     def health_check():
#         return "FastAPI is working!"
