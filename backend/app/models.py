from sqlmodel import Field, SQLModel
from pydantic import BaseModel

### Database tables

class Users(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    username: str
    sha256_password: str
    full_name: str
    name: str
    age: int
    address: str
    email: str

### Generic schemas

class Token(BaseModel):
    access_token: str
    token_type: str

### Request schemas

class UserCreateRequest(SQLModel):
    username: str
    password: str
    full_name: str
    name: str
    age: int
    address: str
    email: str

class UserUpdateRequest(SQLModel):
    username: str | None = None
    full_name: str | None = None
    name: str | None = None
    age: int | None = None
    address: str | None = None
    email: str | None = None


### Response schemas

class GenericResponse(SQLModel):
    status: str
    details: dict = {}

class ListResponse(SQLModel):
    status: str
    details: list
    metadata: dict = {} 

class UserDetailsResponse(SQLModel):
    user_id: int
    username: str
    full_name: str
    name: str
    age: int
    address: str
    email: str
