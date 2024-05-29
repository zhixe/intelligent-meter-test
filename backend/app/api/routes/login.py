from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from sqlmodel import Session, select

from core.main import engine
from core.security import create_access_token
from utils import hash_password
from models import Token, Employees, Customers

router = APIRouter()

### Login using Oauth2

@router.post('')
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    
    auth_tables = [Employees, Customers]
    user_class = None
    
    with Session(engine) as session:

        for table in auth_tables:

            statement = select(table).where(table.username == form_data.username)
            results = session.exec(statement)
            user = results.first()

            if not user:
                continue

            elif user.password != hash_password(form_data.password):
                continue
            else:
                user_class = table
                break
        
        if user_class is not None:
            if user_class == Customers:
                return Token(
                    access_token=create_access_token(user.customer_id),
                    token_type='bearer'
                )
            elif user_class == Employees:
                return Token(
                    access_token=create_access_token(user.employee_id),
                    token_type='bearer'
                )