from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from sqlmodel import Session, select

from core.main import engine
from core.security import create_access_token
from utils import hash_password
from models import Users, Token

router = APIRouter()

### Login using Oauth2

@router.post('/login')
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    with Session(engine) as session:
        statement = select(Users).where(Users.username == form_data.username)
        results = session.exec(statement)

        user = results.first()

        if not user:
            raise HTTPException(status_code=400, detail='Incorrect username or password')

        elif user.sha256_password != hash_password(form_data.password):
            raise HTTPException(status_code=400, detail='Incorrect username or password')

        return Token(
            access_token=create_access_token(user.username),
            token_type='bearer'
        )