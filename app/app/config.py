from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(env="DATABASE_URL")
    SECRET_KEY: str = Field(env="SECRET_KEY")


settings = Settings()