from connect_db import Base, engine, Session
from sqlalchemy import  Table, Column, Integer, String, JSON, Index, MetaData

import json
class Review(Base):
    meta = MetaData()
    data = Table(
        'data', meta,
        Column('id', Integer,pimary_key=True),
        Column('name_english', String(1000)),
        Column('name_japanese', String(1000)),
        Column('name_chinese', String(1000)),
        Column('name_french', String(1000)),
        Column('type', JSON),
        Column('base_HP', Integer),
        Column('base_Attack', Integer),
        Column('base_Defense', Integer),
        Column('base_Sp_Attack', Integer),
        Column('base_Sp_Defense', Integer),
        Column('base_Speed', Integer),
        Index("some_index", "id","name_english", "name_japanese", "name_chinese", "name_french", "type", "base_HP",\
                             "base_Attack", "base_Defense", "base_Sp_Attack", "base_Sp_Defense", "base_Speed")
    )
Base.metadata.create_all(engine)

def json_to_database(eng):
    with eng.connect()as conn:

        try:
            with open('pokedex.json') as f:
                sql = f.read()
                json_data = json.loads(sql)
                r = Review(int(json_data['id']), json_data['name_english'],
                           json_data['name_japanese'], json_data['name_chinese'],
                           json_data['name_french'], json_data['type'],
                           int(json_data['base_HP']), int(json_data['base_Attack']),
                           int(json_data['base_Defense']), int(json_data['base_Sp_Attack']),
                           int(json_data['base_Sp_Defense']), int(json_data['base_Speed']))
                Session.add(r)
                Session.commit()

        except ValueError as err:
            return False


json_to_database(engine)