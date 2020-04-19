from app.api import crud
from app.api import token_service
from app.api.models import TokenResponse, TokenRequest
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/token", response_model=TokenResponse, status_code=201)
async def create_note(auth: TokenRequest):

    if not await crud.get_user(auth.username, auth.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password.")

    return {"key": token_service.create_token(data={"username": auth.username})}
