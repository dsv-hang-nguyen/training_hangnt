
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from airlines_conn import engine
import csv
import sqlalchemy as sqAl

metadata = sqAl.MetaData()
metadata.bind = engine
def export(table,file_name):
    mytable = sqAl.Table(table, metadata, autoload=True)
    db_connection = engine.connect()

    select = sqAl.sql.select([mytable])
    result = db_connection.execute(select)

    fh = open(file_name, 'w+')
    outcsv = csv.writer(fh)

    outcsv.writerow(result.keys())
    outcsv.writerows(result)

    fh.close

if __name__ == "__main__":
    table = str(input())
    file_name = input()
    export(table,file_name)