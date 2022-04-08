from pydantic import BaseSettings, Field

__all__ = ["settings"]


class Settings(BaseSettings):
    debug: bool = Field(False, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
