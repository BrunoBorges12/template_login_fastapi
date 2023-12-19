from pydantic_settings import BaseSettings


class  Settings(BaseSettings):
    PROJECT_NAME:str = 'Login template'



settings = Settings()