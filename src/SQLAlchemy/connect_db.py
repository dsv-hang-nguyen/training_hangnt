from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from config import config
from sqlalchemy.util import IdentitySet

sys.path.append("..")

engine = create_engine("mysql+pymysql://" + config.user + ":" + config.password + "@" + config.host + ":" + config.port + "/" + config.database+"?charset=utf8?use_unicode=True",pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
#
# session = Session()
# c = engine.connect()

# c.execute('ALTER TABLE data MODIFY\
#             name_japanese  varchar(100)\
#             CHARACTER SET utf8\
#             COLLATE utf8_unicode_ci;')
# c.execute('ALTER TABLE data MODIFY\
#             name_chinese  VARCHAR (100)\
#             CHARACTER SET utf8\
#             COLLATE utf8_unicode_ci;')
#
# # suppose the database has been restarted.
# c.execute("INSERT INTO data VALUES (1,'Bulbasaur','フシギダネ','妙蛙种子','Bulbizarre','Grass-Poison',45,49,49,65,65,45)")
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(50))
#     fullname = Column(String(50))
#     nickname = Column(String(50))
#
# Base.metadata.create_all(engine)
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# # session.add(ed_user)
# # session.add_all([User(name='wendy', fullname='Wendy Williams', nickname='windy'),\
# #                  User(name='mary', fullname='Mary Contrary', nickname='mary'),\
# #                  User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
# ed_user.nickname = 'eddie'
# session.dirty
# IdentitySet(User(name='ed', fullname='Ed Jones', nickname='eddie'))
# session.new
# IdentitySet(User(name='wendy', fullname='Wendy Williams', nickname='windy'),\
#             User(name='mary', fullname='Mary Contrary', nickname='mary'),\
#             User(name='fred', fullname='Fred Flintstone', nickname='freddy'))
# session.commit()
# session.close()
# c.close()
