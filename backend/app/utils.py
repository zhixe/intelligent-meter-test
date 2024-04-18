import yaml
import hashlib

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