from datetime import datetime, timedelta, timezone

import jwt

from utils import load_yaml

config = load_yaml('./core/security.yaml')

SECRET_KEY = config['jwt_secret']
ALGORITHM = 'HS256'

def create_access_token(subject: str, expires_delta: timedelta | None = None):

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode = ({"exp": expire, "sub": subject})
    
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 