import configparser
import urllib.parse
config_parser = configparser.ConfigParser()
config_parser.read('env.ini')
ENV = config_parser.get('APP', 'env')
APP_PORT = 5000




"""For Local"""
DB_TYPE = urllib.parse.quote_plus(config_parser.get(ENV, 'DB_TYPE'))
DB_USER =urllib.parse.quote_plus(config_parser.get(ENV, 'POSTGRES_USER'))
DB_PWD =urllib.parse.quote_plus(config_parser.get(ENV, 'POSTGRES_PASSWORD'))
DB_HOST = urllib.parse.quote_plus(config_parser.get(ENV, 'POSTGRES_HOSTNAME'))
DB_NAME =urllib.parse.quote_plus(config_parser.get(ENV, 'POSTGRES_DB_NAME'))
DB_URL = f"{DB_TYPE}://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}"

