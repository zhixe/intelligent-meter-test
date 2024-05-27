from fastapi import APIRouter
from sqlmodel import Session, select

from core.main import engine
from models import GenericResponse

router = APIRouter()

@router.get("/db/health_check")
async def test_connection() -> GenericResponse:

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

    return GenericResponse(
        status=status, 
        details={'message': message}
    )
