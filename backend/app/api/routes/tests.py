from fastapi import APIRouter
from sqlmodel import Session, select

from core.main import engine
from models import StatusResponse

router = APIRouter()

@router.get("/connection")
async def test_connection() -> StatusResponse:

    status = None

    try:
        session = Session(engine)
        session.exec(select(1))
        session.close()

        status = 'OK'
        message = 'Connection successful'

    except Exception as e:
        status = 'ERROR'
        message = str(e)

    return StatusResponse(status=status, message=message)
