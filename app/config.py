from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_name:str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 60


    class Config:
        env_file = ".env"

settings=Settings()
