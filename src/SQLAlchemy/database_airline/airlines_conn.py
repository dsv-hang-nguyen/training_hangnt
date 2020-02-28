from airlines_db import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


sys.path.append("..")

engine = create_engine("mysql+pymysql://" + config.user + ":" + config.password + "@" + config.host + ":" + config.port + "/" + config.database+"?charset=utf8?use_unicode=True",pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
