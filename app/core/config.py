import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class settings(BaseSettings):
    DATABASE_URL: str = (
        f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE_NAME')}?sslmode={os.getenv('SSL_MODE')}"
    )

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")


settings = settings()
