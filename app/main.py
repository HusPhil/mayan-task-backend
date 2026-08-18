from fastapi import FastAPI
from app.api.router import v1_router
from app.core.config import settings

is_development = settings.ENVIRONMENT == "development"

app = FastAPI(
    title="Mayan Task Management API", docs_url="/docs" if is_development else None
)

app.include_router(prefix="/api", router=v1_router)


if is_development:

    @app.get("/")
    def health_check():
        return "FastAPI is working!"
