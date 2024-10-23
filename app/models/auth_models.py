from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., description="The login username", example="mercadobitcoin@gmail.com")
    password: str = Field(..., description="the password to user", example="mercadobitcoin2024")

class LoginResponse(BaseModel):
    access_token: str = Field(..., description="JWT access token generated after successful login")
