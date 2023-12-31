from app.api import crud
from app.api import key_service
from app.api.models import TokenResponse, TokenRequest
from fastapi import APIRouter, HTTPException
from app.api import hashing_service

router = APIRouter()


@router.post("/token", response_model=TokenResponse, status_code=201)
async def create_token(auth: TokenRequest):

    if not await crud.get_user(auth.username, hashing_service.hash(auth.password)):
        raise HTTPException(status_code=401, detail="Incorrect username or password.")

    return {"key": key_service.encode_key(data={"username": auth.username})}
