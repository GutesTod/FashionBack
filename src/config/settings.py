from pydantic_settings import BaseSettings

class SettingsBack(BaseSettings):
    POSTGRES_URL: str
    CLICKHOUSE_URL: str

    class Config:
        env_file = "././.env"
        env_encoding = "utf-8"

settings = SettingsBack()
