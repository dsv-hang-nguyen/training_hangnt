from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from airlines_conn import Base

import sys
sys.path.append("..")

class top10_dl_fl(Base):
    __tablename__ = "top10_delayed_flight_airports"

    id = Column(Integer, primary_key=True)
    airport_name = Column(String(100))
    count_delay = Column(Integer)
    def __init__(self, airport_name, count_delay):
        self.airport_name = airport_name
        self.count_delay = count_delay

class top10_airport_minutes_delayed(Base):
    __tablename__ = "top10_airport_minutes_delayed"

    id = Column(Integer, primary_key=True)
    airport_name = Column(String(100))
    minutes_delay = Column(Integer)
    def __init__(self, airport_name, minutes_delay):
        self.airport_name = airport_name
        self.minutes_delay = minutes_delay

class top10_city_delayed(Base):
    __tablename__ = "top10_delayed_flight_cities"

    id = Column(Integer, primary_key=True)
    city = Column(String(100))
    count_delay = Column(Integer)
    def __init__(self, city, count_delay):
        self.city = city
        self.count_delay = count_delay

class top10_minute_delayed_flight_cities(Base):
    __tablename__ = "top10_minute_delayed_flight_cities"

    id = Column(Integer, primary_key=True)
    city = Column(String(100))
    airport_name = Column(String(100))
    minutes_delay = Column(Integer)

    def __init__(self, city, airport_name, minutes_delay):
        self.city = city
        self.airport_name = airport_name
        self.minutes_delay = minutes_delay


