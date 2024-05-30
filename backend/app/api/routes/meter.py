from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlmodel import Session, select

from core.main import engine
from core.security import decode_access_token
from models import Meters, ListResponse

router = APIRouter()


@router.get('')
async def get_meter(meter_serial: str):
    
    with Session(engine) as session:

        statement = select(Meters).where(Meters.meter_serial == meter_serial)

        results = session.exec(statement)

        meter = results.first()
        meter = Meters(**meter.model_dump())

        return meter
    


@router.get('/all')
async def get_all_meters(offset: int = 0, limit: int = 10):

    if limit > 1000:
        limit = 1000

    with Session(engine) as session:

        statement = select(Meters).offset(offset).limit(limit)

        results = session.exec(statement)
        meters = results.all()

        return ListResponse(
            status='OK',
            details=meters
        )


@router.put('/insert')
async def create_meter(meter: Meters):
    
    with Session(engine) as session:

        new_meter = Meters(**meter.model_dump())

        session.add(new_meter)
        session.commit()

        return new_meter