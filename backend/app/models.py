from sqlmodel import Field, SQLModel
from pydantic import BaseModel
# from typing import Annotated
from fastapi import Form

from typing_extensions import Annotated, Doc

from datetime import datetime, timezone

def current_timestamp():
    return datetime.now(timezone.utc).timestamp()

### Database tables

class Login_credentials(SQLModel, table=True):
    username: str = Field(primary_key=True)
    password: str
    login_attempt: int
    last_login: int

class Users(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    username: str
    sha256_password: str
    full_name: str
    name: str
    age: int
    address: str
    email: str

class Customers(SQLModel, table=True):
    customer_id: str | None = Field(default=None, primary_key=True)
    meter_serial: str | None
    username: str = Field(foreign_key="login_credentials.username")
    customer_email: str
    first_name: str
    last_name: str
    address: str
    ic_no: str
    phone_no: str
    age: int

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

class RegisterCustomerForm:

    def __init__(
            self, 
            username: Annotated[str, Form()],
            password: Annotated[str, Form()],
            customer_email: Annotated[str, Form()],
            first_name: Annotated[str, Form()],
            last_name: Annotated[str, Form()],
            address: Annotated[str, Form()],
            ic_no: Annotated[str, Form()],
            phone_no: Annotated[str, Form()],
            age: Annotated[int, Form()]
            ):
        self.username = username
        self.password = password
        self.customer_email = customer_email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.ic_no = ic_no
        self.phone_no = phone_no
        self.age = age


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
