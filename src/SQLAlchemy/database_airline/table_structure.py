from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from airlines_conn import Base

import sys
sys.path.append("..")

class Product_al(Base):

    __tablename__ = "carrier"
    id = Column(Integer, primary_key=True)
    code = Column(String(30))
    name = Column(String(30))

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def to_string(self):
        return "id: " + str(self.id) + " code: "+ str(self.code) + "name:", self.name

class Statistics_flights(Base):

    __tablename__ = "statistics_flights"

    id = Column(Integer, primary_key=True)
    cancelled = Column(Integer)
    on_time = Column(Integer)
    total = Column(Integer)
    delayed = Column(Integer)
    diverted = Column(Integer)
    product_id = Column(Integer, ForeignKey('carrier.id'))
    product = relationship("Product_al", backref=backref("statistics_flights", uselist=False))

    def __init__(self, cancelled, on_time, total, delayed, diverted, product):
        self.cancelled = cancelled
        self.on_time = on_time
        self.total = total
        self.delayed = delayed
        self.diverted = diverted
        self.product = product

class Statistics_delays(Base):
    __tablename__ = "statistics_delays"
    id = Column(Integer, primary_key=True)
    late_aircraft = Column(Integer)
    weather = Column(Integer)
    security = Column(Integer)
    national_aviation_system = Column(Integer)
    carrier = Column(Integer)
    product_id = Column(Integer, ForeignKey('carrier.id'))
    product = relationship("Product_al", backref=backref("statistics_delays", uselist=False))

    def __init__(self, late_aircraft, weather, security, national_aviation_system, carrier, product):
        self.late_aircraft = late_aircraft
        self.weather = weather
        self.security = security
        self.national_aviation_system = national_aviation_system
        self.carrier = carrier
        self.product = product
class Statistics_minutes_delayed(Base):
    __tablename__ = "statistics_minutes_delays"
    id = Column(Integer, primary_key=True)
    late_aircraft = Column(Integer)
    weather = Column(Integer)
    carrier = Column(Integer)
    security = Column(Integer)
    total = Column(Integer)
    national_aviation_system = Column(Integer)
    product_id = Column(Integer, ForeignKey('carrier.id'))
    product = relationship("Product_al", backref=backref("statistics_minutes_delays", uselist=False))

    def __init__(self, late_aircraft, weather,carrier, security, total, national_aviation_system, product):
        self.late_aircraft = late_aircraft
        self.weather = weather
        self.carrier = carrier
        self.security = security
        self.total = total
        self.national_aviation_system = national_aviation_system
        self.product = product
class Time(Base):

    __tablename__ = "time"

    id = Column(Integer, primary_key=True)
    label = Column(String(100))
    year = Column(Integer)
    month = Column(Integer)
    product_id = Column(Integer, ForeignKey('carrier.id'))
    product = relationship("Product_al", backref=backref("time",  uselist=False))


    def __init__(self, label, year,month, product):
        self.label = label
        self.year = year
        self.month = month
        self.product = product



class Airport(Base):

    __tablename__ = "airport"

    id = Column(Integer, primary_key=True)
    code = Column(String(100))
    name = Column(String(100))
    city = Column(String(100))
    product_id = Column(Integer, ForeignKey('carrier.id'))
    product = relationship("Product_al", backref=backref("airport",  uselist=False))


    def __init__(self, code, name,city, product):
        self.code = code
        self.name = name
        self.city = city
        self.product = product

