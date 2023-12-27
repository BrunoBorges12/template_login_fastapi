from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Login template"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8


settings = Settings()
