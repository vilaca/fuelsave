import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta
from app.settings import settings


def encode_key(
    *, data: dict, delta: timedelta = timedelta(minutes=settings.TOKEN_TTL_MINUTES)
):
    to_encode = data.copy()
    expire = datetime.utcnow() + delta
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    ).decode("utf-8")


def decode_key(key: str):
    try:
        payload = jwt.decode(key, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise AuthenticationError("Could not validate credentials - no user")
        return username
    except PyJWTError as e:
        raise AuthenticationError(str(e))


class AuthenticationError(Exception):
    pass
