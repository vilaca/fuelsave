from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    key: str = Field(...)


class TokenRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)
