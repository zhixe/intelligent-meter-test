from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from sqlmodel import Session, select

from core.main import engine
from core.security import decode_access_token

from utils import hash_password
from models import EmployeeDetailsResponse, CustomerDetailsResponse, Customers, Employees

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get('/me')
async def get_current_user(token: str = Depends(oauth2_scheme)):

    object = decode_access_token(token)

    if object['sub'].startswith('CUST'):
        user_class = Customers
    elif object['sub'].startswith('EMPL'):
        user_class = Employees

    user_id = object['sub']
    
    with Session(engine) as session:

        if user_class == Customers:
            statement = select(Customers).where(Customers.customer_id == user_id)
            results = session.exec(statement)
            user = results.first()
            user = CustomerDetailsResponse(**user.model_dump())        
        elif user_class == Employees:
            statement = select(Employees).where(Employees.employee_id == user_id)
            results = session.exec(statement)
            user = results.first()
            user = EmployeeDetailsResponse(**user.model_dump())

        return user