import hashlib
import base64
from app.settings import settings


def hash(plaintext: str):
    return base64.b64encode(
        hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), settings.PASSWORD_SALT.encode(), 190420
        )
    ).decode()


def compare(plaintext: str, encoded: str):
    return hash(plaintext) == encoded
