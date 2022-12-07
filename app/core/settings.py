from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_URL: str
    FUNCTION_URL: str
    SECRET_KEY: str
    ALGORITHM: str


settings = Settings(_env_file=".env")
