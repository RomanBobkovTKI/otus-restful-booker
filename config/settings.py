import os
from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT_DIR / ".env"

load_dotenv(ENV_FILE)


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
    TIMEOUT = int(os.getenv("TIMEOUT", 10))
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    @classmethod
    def validate(cls):
        required_vars = {
            "BASE_URL": cls.BASE_URL,
            "USERNAME": cls.USERNAME,
            "PASSWORD": cls.PASSWORD,
        }

        missing_vars = [
            name for name, value in required_vars.items()
            if not value
        ]

        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )


settings = Settings()
settings.validate()