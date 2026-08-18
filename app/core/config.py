import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = (
        f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE_NAME')}?sslmode=require"
    )

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")


settings = Settings()
