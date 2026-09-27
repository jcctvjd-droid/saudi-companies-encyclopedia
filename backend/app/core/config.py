from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Saudi Companies Encyclopedia"
    app_env: str = "development"
    debug: bool = True
    api_base_url: str = "http://localhost:8000"
    secret_key: str = "change-me-in-production"

    postgres_host: str = "postgres"
    postgres_port: int = 5432
    postgres_db: str = "saudi_companies"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    database_url: str = "postgresql+psycopg2://postgres:postgres@postgres:5432/saudi_companies"

    redis_url: str = "redis://redis:6379/0"
    opensearch_url: str = "http://opensearch:9200"
    opensearch_username: str = "admin"
    opensearch_password: str = "admin"

    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
