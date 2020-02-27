from connect_db import engine, Session, Base
from product import Product, Details, Names
import json

Base.metadata.create_all(engine)
session = Session()
c = engine.connect()
c.execute('ALTER TABLE names MODIFY\
            value VARCHAR (100)\
            CHARACTER SET utf8\
            COLLATE utf8_unicode_ci;')

f = open('pokedex.json')
sql = f.read()
json_data = json.loads(sql)
for element in json_data:
    type_of_product = ""
    for i in element['type']:
        type_of_product += i

    product = Product(type_of_product)
    eng_name = Names("english", element['name']['english'], product)
    jpa_name = Names("japanese", element['name']['japanese'], product)
    chie_name = Names("chinese", element['name']['chinese'], product)
    fr_name = Names("french", element['name']['french'], product)

    detail = Details(element['base']['HP'],
                     element['base']['Attack'],
                     element['base']['Defense'],
                     element['base']['Sp. Attack'],
                     element['base']['Sp. Defense'],
                     element['base']['Speed'], product)


    session.add(product)
    session.add(eng_name)
    session.add(jpa_name)
    session.add(chie_name)
    session.add(fr_name)
    session.add(detail)


session.commit()
session.close()