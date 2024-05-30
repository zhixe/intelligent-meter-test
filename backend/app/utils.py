import yaml
import random
import hashlib
from models import Customers, Employees, Meters
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
        'employee':{
            'prefix': 'EMPL',
            'table': Employees,
            'column': 'employee_id'
        },
        'meter': {
            'prefix': 'METR',
            'table': Meters,
            'column': 'meter_serial'
        },
        # 'tracking': 'TRKG'
    }

    type_ = mapping[id_type]

    statement = select(
        getattr(type_['table'], type_['column'])
    )

    with Session(engine) as session:
        results = session.exec(statement).all()

    while True:

        id_ = type_['prefix'] + '%07d' % random.randint(0, 9999999)

        if id_ not in results:
            return id_