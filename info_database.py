"""Config values."""
from os import environ
class Config:
    # Database config
    db_user = environ.get('root')
    db_password = environ.get('123456')
    db_host = environ.get('localhost')
    db_port = environ.get('')
    db_name = environ.get('airlines')