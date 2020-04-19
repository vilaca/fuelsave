import os


class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    TOKEN_TTL_MINUTES = int(os.getenv("TOKEN_TTL_MINUTES", 10))
    DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()
