from fastapi import APIRouter
from sqlmodel import Session, select

from core.main import engine
from utils import hash_password
from models import Users, UserCreateRequest, UserDetailsResponse, UserCreateResponse, UserUpdateRequest, UserUpdateResponse

router = APIRouter()

@router.get('/details')
async def get_user_details(user_id: str) -> UserDetailsResponse:

    with Session(engine) as session:

        statement = select(Users).where(Users.user_id == user_id)
        results = session.exec(statement)

        user = results.first()
        user = UserDetailsResponse(**user.model_dump())

        return user

@router.post('/create')
async def create_user(user: UserCreateRequest) -> UserCreateResponse:

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

        user_details = UserDetailsResponse(**new_user.model_dump())

        session.commit()

    return UserCreateResponse(
        status='OK',
        user_details=user_details
    )
        


@router.put('/update')
async def update_user(user_id: int, user: UserUpdateRequest, force_nulls: bool = False) -> UserUpdateResponse:

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

    return UserUpdateResponse(status='OK')