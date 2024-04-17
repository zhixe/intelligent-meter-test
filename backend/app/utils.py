import yaml

CONFIG_FILENAME = 'config.yaml'

def load_config():

    with open(CONFIG_FILENAME, 'r') as f:
        config = yaml.safe_load(f)

    return config