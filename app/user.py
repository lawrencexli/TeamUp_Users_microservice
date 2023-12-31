from typing import List, Optional, Annotated
from pydantic import BaseModel, Field, EmailStr, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class UserModel(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    email: EmailStr = Field(...)
    contact: str = Field(...)
    location: str = Field(...)
    interests: List[str] = Field(...)
    age: Optional[int] = Field(..., ge=13, le=150)
    gender: str = Field(...)


class UserFullModel(UserModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    friends: List[str] = Field(...)


class UserWithJWT(UserFullModel):
    access_token: str


class UserWithPwd(UserFullModel):
    password: str = Field(..., min_length=8)


class UserFriendsModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    friends: List[str] = Field(...)


class UpdateUserModel(BaseModel):
    first_name: Optional[str] = Field(default=None, max_length=30)
    last_name: Optional[str] = Field(default=None, max_length=30)
    contact: Optional[str] = None
    location: Optional[str] = None
    interests: Optional[List[str]] = None
    age: Optional[int] = Field(default=None, ge=13, le=150)
    gender: Optional[str] = None
    friends: Optional[List[str]] = None


class UpdateUsername(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)


class UserCollection(BaseModel):
    users: List[UserModel]
