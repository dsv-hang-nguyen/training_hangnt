from sqlalchemy import create_engine, cast, String, type_coerce, JSON, PrimaryKeyConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import exc, sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData
import json
"""Connect to MySQL Database."""
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/pokedex')
Base = declarative_base()

class Review(Base):
    meta = MetaData()
    # __tablename__ = 'Review'
    # __table_args__ = (
    #     PrimaryKeyConstraint('id','name_english', 'name_japanese', 'name_chinese', 'name_french', 'type', 'base_HP',\
    #                          'base_Attack', 'base_Defense', 'base_Sp_Attack', 'base_Sp_Defense', 'base_Speed'),
    # )
    # data = Table(
    #     'data', meta,
    #     Column('id', Integer),
    #     Column('name_english', String(1000)),
    #     Column('name_japanese', String(1000)),
    #     Column('name_chinese', String(1000)),
    #     Column('name_french', String(1000)),
    #     Column('type', String(1000)),
    #     Column('base_HP', Integer),
    #     Column('base_Attack', Integer),
    #     Column('base_Defense', Integer),
    #     Column('base_Sp_Attack', Integer),
    #     Column('base_Sp_Defense', Integer),
    #     Column('base_Speed', Integer),
    #     Index("some_index", "id","name_english", "name_japanese", "name_chinese", "name_french", "type", "base_HP",\
    #                          "base_Attack", "base_Defense", "base_Sp_Attack", "base_Sp_Defense", "base_Speed")
    # )
    # meta.create_all(engine)

    data = Table(
        'data', meta,
        id = Column(Integer),
        name_english = Column(String(1000)),
        name_japanese = Column(String(1000)),
        name_chinese = Column(String(1000)),
        name_french = Column(String(1000)),
        type = Column(JSON),
        base_HP = Column(Integer),
        base_Attack = Column(Integer),
        base_Defense = Column(Integer),
        base_Sp_Attack = Column(Integer),
        base_Sp_Defense = Column(Integer),
        base_Speed = Column(Integer)
    )

    # def __init__(self, id,name_english,name_japanese,name_chinese,name_french,type,base_HP,base_Attack,base_Defense,base_Sp_Attack,base_Sp_Defense,base_Speed):
    #     """"""
    #     self.id = id
    #     self.name_english = name_english
    #     self.name_japanese = name_japanese
    #     self.name_chinese = name_chinese
    #     self.name_french = name_french
    #     self.type = type
    #     self.base_HP = base_HP
    #     self.base_Attack = base_Attack
    #     self.base_Defense = base_Defense
    #     self.base_Sp_Attack = base_Sp_Attack
    #     self.base_Sp_Defense = base_Sp_Defense
    #     self.base_Speed =base_Speed

# create tables
Base.metadata.create_all(engine)

def json_to_database(eng):
    with eng.connect()as conn:

        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            with open('pokedex.json') as f:
                sql = f.read()
                jsondata = json.loads(sql)

                r = Review(int(jsondata['id']), jsondata['name_english'],\
                           jsondata['name_japanese'], jsondata['name_chinese'],\
                           jsondata['name_french'], jsondata['type'],\
                           int(jsondata['base_HP']), int(jsondata['base_Attack']),\
                           int(jsondata['base_Defense']), int(jsondata['base_Sp_Attack']),\
                           int(jsondata['base_Sp_Defense']), int(jsondata['base_Speed']))
                session.add(r)
                session.commit()

        except ValueError as err:
            return  False
json_to_database(engine)




