from src.app.config.settings import settings


def test_app_name_exists():
    assert settings.APP_NAME != ""


def test_default_env_is_dev():
    assert settings.APP_ENV == "development"
