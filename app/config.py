from pydantic import BaseSettings

class Settings(BaseSettings):
    # env variable is case insensitive

    # DATABASE_HOSTNAME:str
    # DATABASE_PORT:str
    # DATABASE_NAME:str
    # DATABASE_USERNAME:str
    # SECRET_KEY:str
    # ALGORITHM:str
    # ACCESS_TOKEN_EXPIRE_MINUTE:str

    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = "../.env"

settings = Settings()