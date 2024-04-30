from datetime import datetime, timedelta, timezone

import jwt

from utils import load_yaml

config = load_yaml('./core/security.yaml')

JWT_EXPIRE_TIME_HOURS = config['jwt_expire_time_hours']
SECRET_KEY = config['jwt_secret']
ALGORITHM = 'HS256'

def create_access_token(subject: str, expires_delta: timedelta | None = None):

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRE_TIME_HOURS)
    to_encode = ({"expire": expire.timestamp(), "sub": subject})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 

def decode_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return payload