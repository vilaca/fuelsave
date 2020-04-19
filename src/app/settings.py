import os


class Settings:
    ALGORITHM = os.getenv("ALGORITHM")
    DATA_IMPORT_PATH = os.getenv("DATA_IMPORT_PATH")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    TOKEN_TTL_MINUTES = int(os.getenv("TOKEN_TTL_MINUTES", 10))
    PASSWORD_SALT = os.getenv("PASSWORD_SALT")


settings = Settings()
