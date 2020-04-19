from pydantic import BaseModel, Field
from typing import List


class TokenResponse(BaseModel):
    key: str = Field(...)


class TokenRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)


class Vehicle(BaseModel):
    id: int
    distance: int
    owner: str = Field(..., min_length=3, max_length=50)


class VehiclesResponse(BaseModel):
    vehicles: List[Vehicle]
