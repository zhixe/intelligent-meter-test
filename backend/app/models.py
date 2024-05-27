from sqlmodel import Field, SQLModel
from pydantic import BaseModel
# from typing import Annotated
from fastapi import Form

from typing_extensions import Annotated, Doc

from datetime import datetime, timezone

def current_timestamp():
    return datetime.now(timezone.utc).timestamp()

def current_datetime():
    return datetime.now(timezone.utc)

### Database tables
class Employees(SQLModel, table=True):
    employee_id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    department: str
    position: str
    employment_type: str

class Customers(SQLModel, table=True):
    customer_id: str | None = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    address: str
    ic_no: str
    phone_no: str
    age: int

class Meters(SQLModel, table=True):
    meter_serial: str | None = Field(default=None, primary_key=True)
    manufacturer: str
    store_region: str
    size: int
    type: str
    model: str

### Generic schemas

class Token(BaseModel):
    access_token: str
    token_type: str

### Request schemas

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

class RegisterEmployeeForm:

    def __init__(
            self, 
            username: Annotated[str, Form()],
            password: Annotated[str, Form()],
            email: Annotated[str, Form()],
            first_name: Annotated[str, Form()],
            last_name: Annotated[str, Form()],
            department: Annotated[str, Form()],
            position: Annotated[str, Form()],
            employment_type: Annotated[str, Form()]
    ):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.position = position
        self.employment_type = employment_type

### Response schemas

class EmployeeDetailsResponse(SQLModel):
    employee_id: str
    username: str
    email: str
    first_name: str
    last_name: str
    department: str
    position: str
    employment_type: str

class CustomerDetailsResponse(SQLModel):
    customer_id: str
    username: str
    email: str
    first_name: str
    last_name: str
    address: str
    ic_no: str
    phone_no: str
    age: int

class GenericResponse(SQLModel):
    status: str
    details: dict = {}

class ListResponse(SQLModel):
    status: str
    details: list
    metadata: dict = {} 

class StatusResponse(SQLModel):
    success: bool
    timestamp: float = Field(default_factory=current_datetime)
    details: dict = {}

