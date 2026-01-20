import os


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "github-project-setup")
    APP_ENV: str = os.getenv("APP_ENV", "development")


settings = Settings()
