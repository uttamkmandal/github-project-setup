from src.app.core.logger import logger
from src.app.config import settings


def main():
    logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} mode")


if __name__ == "__main__":
    main()
