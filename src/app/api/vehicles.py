from app.api import crud
from app.api import key_service
from app.api.models import VehiclesResponse
from fastapi import APIRouter, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey


router = APIRouter()


async def get_api_key(
    query_string: str = Security(APIKeyQuery(name="api-key", auto_error=False)),
    auth_header: str = Security(APIKeyHeader(name="Authorization", auto_error=False)),
):
    try:
        if query_string:
            key: str = query_string
        else:
            key: str = str(auth_header)
            if not key.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="Bearer expected.")
            key = key[len("Bearer ") :]
        return key_service.decode_key(key)
    except key_service.AuthenticationError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/vehicles", response_model=VehiclesResponse)
async def list_vehicles_for_user(user: APIKey = Depends(get_api_key)):
    return {"vehicles": await crud.get_vehicles(user)}
