from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from sqlmodel import Session, select

from core.main import engine
from core.security import decode_access_token

from utils import hash_password
from models import Users, UserCreateRequest, UserDetailsResponse, UserUpdateRequest, GenericResponse

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get('/me')
async def get_current_user(token: str = Depends(oauth2_scheme)):

    object = decode_access_token(token)

    user_id = object['sub']

    with Session(engine) as session:

        statement = select(Users).where(Users.user_id == user_id)
        results = session.exec(statement)

        user = results.first()
        user = UserDetailsResponse(**user.model_dump())

        return user

@router.get('/details')
async def get_user_details(user_id: str) -> UserDetailsResponse:
    """
    Get details of a user based on the provided user ID.
    """
    with Session(engine) as session:

        statement = select(Users).where(Users.user_id == user_id)
        results = session.exec(statement)

        user = results.first()
        user = UserDetailsResponse(**user.model_dump())

        return user

@router.post('/create')
async def create_user(user: UserCreateRequest, return_userid: bool = False) -> GenericResponse:
    """
    Creates a new user.
    """
    with Session(engine) as session:

        new_user = Users(
            username=user.username,
            sha256_password=hash_password(user.password),
            full_name=user.full_name,
            name=user.name,
            age=user.age,
            address=user.address,
            email=user.email
        )

        session.add(new_user)
        session.flush()
        session.refresh(new_user)

        user_id = new_user.user_id

        session.commit()

        if return_userid:
            return GenericResponse(
                status='OK',
                details={'user_id': user_id}
            )
        else:
            return GenericResponse(
                status='OK'
            )
        


@router.put('/update')
async def update_user(user_id: int, user: UserUpdateRequest, force_nulls: bool = False) -> GenericResponse:
    """
    Update user details based on the provided user ID with optional force_nulls flag.
    """
    with Session(engine) as session:

        statement = select(Users).where(Users.user_id == user_id)
        results = session.exec(statement)

        old_user = results.first()

        for attr in user.model_fields:
            if not force_nulls:
                if getattr(user, attr) is not None and getattr(old_user, attr) != getattr(user, attr):
                    setattr(old_user, attr, getattr(user, attr))
            else:
                setattr(old_user, attr, getattr(user, attr))

        session.commit()

        return GenericResponse(status='OK')