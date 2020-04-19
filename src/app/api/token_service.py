import jwt
from datetime import datetime, timedelta
from app.settings import settings


def create_token(
    *, data: dict, delta: timedelta = timedelta(minutes=settings.TOKEN_TTL_MINUTES)
):
    to_encode = data.copy()
    expire = datetime.utcnow() + delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
