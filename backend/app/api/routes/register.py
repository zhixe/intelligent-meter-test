from typing import Annotated

from fastapi import APIRouter, Form, Depends

from core.main import engine
from models import Customers, RegisterCustomerForm

from sqlmodel import Session

from utils import hash_password, generate_id
from uuid import uuid4




router = APIRouter()

@router.post('/customer')
async def register_customer(
    form_data: Annotated[RegisterCustomerForm, Depends()]
):
    with Session(engine) as session:

        new_customer = Customers(
            customer_id=generate_id(engine, 'customer'),
            username=form_data.username,
            password=hash_password(form_data.password),
            email=form_data.customer_email,
            first_name=form_data.first_name,
            last_name=form_data.last_name,
            address=form_data.address,
            ic_no=form_data.ic_no,
            phone_no=form_data.phone_no,
            age=form_data.age
        )
        
        session.add(new_customer)
        session.commit()

        return

@router.post('/test')
async def test(form_data: Annotated[RegisterCustomerForm, Depends()]):

    return form_data