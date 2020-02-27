
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from connect_db import engine
import csv

Base = automap_base()
Base.prepare(engine, reflect=True)
# Map the tables
Names = Base.classes.names
session = Session(engine, autoflush=False)
def export():

    q = session.query(Names)
    with open('names_table.csv', 'w+') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        header = Names.__table__.columns.keys()

        outcsv.writerow(header)

        for record in q.all():
            outcsv.writerow([getattr(record, c) for c in header ])

if __name__ == "__main__":
    export()