from airlines_conn import engine, Session, Base
from table_structure import Product_al, Statistics_flights, Statistics_delays, Statistics_minutes_delayed,Time, Airport
import json

Base.metadata.create_all(engine)
session = Session()

f = open('airlines.json')
sql = f.read()
json_data = json.loads(sql)
for element in json_data:
    code = ""
    name = ""
    for i in element['carrier']['code']:
        code += i
    for j in element['carrier']['name']:
        name += j

    product = Product_al(code,name)

    statistics_fl = Statistics_flights(element['statistics']['flights']['cancelled'],\
                                   element['statistics']['flights']['on time'],\
                                   element['statistics']['flights']['total'],\
                                   element['statistics']['flights']['delayed'],\
                                   element['statistics']['flights']['diverted'],product)


    statistics_dl = Statistics_delays(element['statistics']['# of delays']['late aircraft'],\
                                         element['statistics']['# of delays']['weather'],\
                                         element['statistics']['# of delays']['security'],\
                                         element['statistics']['# of delays']['national aviation system'],\
                                         element['statistics']['# of delays']['carrier'],product)


    statistics_minute = Statistics_minutes_delayed(  element['statistics']['minutes delayed']['late aircraft'],\
                                                      element['statistics']['minutes delayed']['weather'],\
                                                      element['statistics']['minutes delayed']['carrier'],\
                                                      element['statistics']['minutes delayed']['security'],\
                                                      element['statistics']['minutes delayed']['total'],\
                                                      element['statistics']['minutes delayed']['national aviation system'],product)



    time = Time(element['time']['label'],
                     element['time']['year'],
                     element['time']['month'], product)

    airport = Airport(element['airport']['code'],
                element['airport']['name'].split(",")[1],
                      element['airport']['name'].split(",")[0], product)


    session.add(product)
    session.add(statistics_fl)

    session.add(statistics_dl)

    session.add(statistics_minute)
    session.add(time)
    session.add(airport)


session.commit()
session.close()