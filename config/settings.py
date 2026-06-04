from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    BASE_URL = str(os.getenv("BASE_URL"))
    TIMEOUT = int(os.getenv("TIMEOUT", 10))
    USERNAME = str(os.getenv("USERNAME"))
    PASSWORD = str(os.getenv("PASSWORD"))


settings = Settings()
