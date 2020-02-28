from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from airlines_conn import Base

import sys
sys.path.append("..")

class top10_dl_fl(Base):
    __tablename__ = "top10_delayed_flight_airports_tmp"

    id = Column(Integer, primary_key=True)
    airport_name = Column(String(100))
    count_delay = Column(Integer)
    def __init__(self, airport_name, count_delay):
        self.airport_name = airport_name
        self.count_delay = count_delay
