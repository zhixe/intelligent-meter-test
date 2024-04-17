import yaml
import hashlib

CONFIG_FILENAME = 'config.yaml'

def load_config():

    with open(CONFIG_FILENAME, 'r') as f:
        config = yaml.safe_load(f)

    return config

def hash_password(password: str):

    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return hashed