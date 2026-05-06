from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=64, examples=["admin"])
    email: EmailStr = Field(examples=["admin@example.com"])
    password: str = Field(min_length=6, max_length=128)


class UserLogin(BaseModel):
    username: str = Field(min_length=1, max_length=255, description="Username or email")
    password: str = Field(min_length=1, max_length=128)


class UserRead(BaseModel):
    id: str
    username: str
    email: EmailStr
    is_admin: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserRead
