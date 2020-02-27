from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from connect_db import Base

import sys
sys.path.append("..")


class Product(Base):

    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    type_of_product = Column(String(30))

    def __init__(self, type_of_product):
        self.type_of_product = type_of_product

    def to_string(self):
        return "id: " + str(self.id) + " type: ", self.type_of_product


class Details(Base):

    __tablename__ = "details"

    id = Column(Integer, primary_key=True)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sp_attack = Column(Integer)
    sp_defense = Column(Integer)
    speed = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", backref=backref("details", uselist=False))

    def __init__(self, hp, attack, defense, sp_attack, sp_defense, speed, product):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.product = product


class Names(Base):

    __tablename__ = "names"

    id = Column(Integer, primary_key=True)
    language = Column(String(30))
    value = Column(String(30))
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", backref=backref("names"))


    def __init__(self, language, value, product):
        self.language = language
        self.value = value
        self.product = product