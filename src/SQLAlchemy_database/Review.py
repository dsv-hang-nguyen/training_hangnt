from sqlalchemy import create_engine,cast, String, type_coerce, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import exc, sessionmaker
from sqlalchemy.testing.provision import _pg_drop_db
from sqlalchemy import Table, Column, Integer, String, MetaData
import  pymysql

"""Connect to MySQL Database."""
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/pokedex')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Review(Base):
    meta = MetaData()
    data = Table(
        'data', meta,
        Column('id', Integer, None),
        Column('name_english', String(1000)),
        Column('name_japanese', String(1000)),
        Column('name_chinese', String(1000)),
        Column('name_french', String(1000)),
        Column('type', String(1000)),
        Column('base_HP', Integer, None),
        Column('base_Attack', Integer, None),
        Column('base_Defense', Integer, None),
        Column('base_Sp_Attack', Integer, None),
        Column('base_Sp_Defense', Integer, None),
        Column('base_Speed', Integer, None),
    )
    meta.create_all(engine)