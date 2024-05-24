import yaml
import random
import hashlib
from models import Customers
# from core.main import engine
from sqlmodel import Session, select

CONFIG = 'config.yaml'

def load_yaml(path: str):

    with open(path, 'r') as f:
        config = yaml.safe_load(f)

    return config

def load_config():

    with open(CONFIG, 'r') as f:
        config = yaml.safe_load(f)

    return config

def hash_password(password: str):

    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return hashed

def generate_id(engine, id_type: str):

    mapping = {
        'customer': {
            'prefix': 'CUST',
            'table': Customers,
            'column': 'customer_id'
        },
        'employee': 'EMPL',
        'meter': 'METR',
        'tracking': 'TRKG'
    }

    _type = mapping[id_type]

    statement = select(
        getattr(_type['table'], _type['column'])
    )

    with Session(engine) as session:
        results = session.exec(statement).all()

    while True:

        _id = _type['prefix'] + '%07d' % random.randint(0, 9999999)

        if _id not in results:
            return _id