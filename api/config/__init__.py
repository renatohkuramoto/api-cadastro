import configparser
import os

env = os.getenv('DBENV', 'production')

config_dir = os.path.dirname(__file__)
config = configparser.ConfigParser()
config.read(os.path.join(config_dir, env, 'conf.ini'))


class EnvInterpolation(configparser.BasicInterpolation):
    def before_get(self, parser, section, option, value, defaults):
        value = super().before_get(parser, section, option, value, defaults)
        return os.path.expandvars(value)


def read_config():
    cfg = configparser.ConfigParser(interpolation=EnvInterpolation())
    root = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(root, env, 'config.ini')
    if os.path.isfile(config_file):
        cfg.read(config_file)
        return cfg
    else:
        return None


def get_database():
    cfg = read_config()
    nome = 'database'
    if nome in cfg:
        cfg = cfg[nome]
        return cfg
    else:
        raise Exception('Configuração não localizada.')


def get_secret_key():
    config = read_config()
    if 'secret' in config:
        return config['secret']
    else:
        raise Exception('Secret não definido no config.')


def get_viacep():
    config = read_config()
    if 'viacep' in config:
        return config['viacep']
    else:
        raise Exception('Viacep não definido no config.')
