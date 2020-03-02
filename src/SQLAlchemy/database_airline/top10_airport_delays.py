from airlines_conn import engine, Session, Base
from sqlalchemy.sql import func
from models_db import top10_dl_fl, top10_airport_minutes_delayed, top10_city_delayed, top10_minute_delayed_flight_cities
from table_structure import Statistics_flights, Airport, Statistics_minutes_delayed
from sqlalchemy import distinct
Base.metadata.create_all(engine)
session = Session()

def top10delay():
    i = 0
    for element, count in session.query(Airport.name, func.sum(Statistics_flights.delayed)).join(Statistics_flights , Airport.product_id == Statistics_flights.product_id)\
            .group_by(Airport.name).order_by(func.sum(Statistics_flights.delayed).desc()):
        i += 1
        if i<=10:
            top10query = top10_dl_fl(element, count)
            session.add(top10query)
    session.commit()
    session.close()

def top10airport_minute_delayed():
    i = 0
    for element, sum in session.query(Airport.name, func.sum(Statistics_minutes_delayed.total)).join(Statistics_minutes_delayed, Airport.product_id == Statistics_minutes_delayed.product_id)\
            .group_by(Airport.name).order_by(func.sum(Statistics_minutes_delayed.total).desc()):
        i += 1
        if i<=10:
            top10query = top10_airport_minutes_delayed(element, sum)
            session.add(top10query)

    session.commit()
    session.close()

def top10city_delayed():
    i = 0
    for element, count in session.query(Airport.city, func.sum(Statistics_flights.delayed)).join(Statistics_flights , Airport.product_id == Statistics_flights.product_id)\
            .group_by(Airport.city).order_by(func.sum(Statistics_flights.delayed).desc()):
        i += 1
        if i<=10:
            top10query = top10_city_delayed(element, count)
            session.add(top10query)
    session.commit()
    session.close()

def top10_delayed_airport_minute():
    i = 0
    for element_name,element_city, sum in session.query(Airport.name, top10_city_delayed.city,\
                                                       func.sum(Statistics_minutes_delayed.total))\
            .join(Statistics_minutes_delayed, Airport.product_id == Statistics_minutes_delayed.product_id)\
            .join(top10_city_delayed, Airport.city == top10_city_delayed.city)\
            .group_by(Airport.name, top10_city_delayed.city).order_by(func.sum(Statistics_minutes_delayed.total).desc()):
        i += 1
        if i<=10:
            top10query = top10_minute_delayed_flight_cities(element_city, element_name, sum)
            session.add(top10query)
    session.commit()
    session.close()

if __name__ == "__main__":
    # top10delay()
    # top10airport_minute_delayed()
    # top10city_delayed()
    top10_delayed_airport_minute()