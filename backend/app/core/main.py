from utils import load_config
from sqlmodel import create_engine

def parse_db_uri():
    config = load_config()

    host = config['database']['host']
    port = config['database']['port']
    user = config['database']['user']
    password = config['database']['password']
    db = config['database']['db']

    uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    return uri

### Main section

engine = create_engine(
    url=parse_db_uri(), 
    echo=load_config()['debug']
)