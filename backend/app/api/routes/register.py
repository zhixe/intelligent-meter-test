from typing import Annotated

from fastapi import APIRouter, Form, Depends

from core.main import engine
from models import Customers, RegisterCustomerForm, Login_credentials

from sqlmodel import Session

from utils import hash_password

from uuid import uuid4



router = APIRouter()

@router.post('/customer')
async def register_customer(
    form_data: Annotated[RegisterCustomerForm, Depends()]
):
    
    
    with Session(engine) as session:

        new_credentials = Login_credentials(
            username=form_data.username,
            password=hash_password(form_data.password),
            login_attempt=None,
            last_login=None
        )
        
        session.add(new_credentials)
        session.flush()
        session.refresh(new_credentials)


        new_customer = Customers(
            customer_id=uuid4().hex,
            username=form_data.username,
            customer_email=form_data.customer_email,
            first_name=form_data.first_name,
            last_name=form_data.last_name,
            address=form_data.address,
            ic_no=form_data.ic_no,
            phone_no=form_data.phone_no,
            age=form_data.age
        )

        session.add(new_customer)
        session.flush()
        session.refresh(new_customer)

        session.commit()

        return

@router.post('/test')
async def test(form_data: Annotated[RegisterCustomerForm, Depends()]):

    return form_data