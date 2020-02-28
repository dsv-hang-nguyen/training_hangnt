from airlines_conn import engine, Session, Base
from sqlalchemy.sql import func
from models_db import top10_dl_fl
from table_structure import Statistics_flights, Airport
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
if __name__ == "__main__":
    top10delay()
