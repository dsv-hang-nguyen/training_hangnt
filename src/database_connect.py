import sys
import pymysql
import logging

from matplotlib.rcsetup import validate_string

"""Config values."""
from os import environ
from info_database import Config
import pymysql, os, json

file = os.path.abspath('/home/hangnt/training_hangnt/src/') + "/pokedex.json"
json_data = open(file).read()
json_obj = json.loads(json_data)
class Database:
    """Database connection class."""

    def __init__(self, config):
        self.host = config.db_host
        self.username = config.db_user
        self.password = config.db_password
        self.port = config.db_port
        self.dbname = config.db_name
        self.conn = None
        print(self.host,self.username,self.password,self.port,self.dbname)
        Database.run_query()

    """Database connection class."""


    # read JSON file which is in the next parent folder
    from matplotlib.rcsetup import validate_string


    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(self.host,
                                            user=self.username,
                                            passwd=self.password,
                                            db=self.dbname,
                                            connect_timeout=5)
        except pymysql.MySQLError as e:
            logging.error(e)
            sys.exit()
        finally:
            logging.info('Connection opened successfully.')

    def run_query(self):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
        # parse json data to SQL insert
                for i, item in enumerate(json_obj):
                    id = validate_string(item.get("id", None))
                    name_english = validate_string(item.get("name_english", None))
                    name_japanese = validate_string(item.get("name_japanese", None))
                    name_chinese = validate_string(item.get("name_chinese", None))
                    name_french = validate_string(item.get("name_french", None))
                    type = validate_string(item.get("type", None))
                    base_HP = validate_string(item.get("base_HP", None))
                    base_Attack = validate_string(item.get("base_Attack", None))
                    base_Defense = validate_string(item.get("base_Defense", None))
                    base_Sp_Attack = validate_string(item.get("base_Sp_Attack", None))
                    base_Sp_Defense = validate_string(item.get("base_Sp_Defense", None))
                    base_Speed = validate_string(item.get("base_Speed", None))

                    cur.execute("create table data(`id` INT NULL,`name_english` VARCHAR(MAX) NULL,`name_japanese` VARCHAR(MAX) NULL,\
                                        `name_chinese` VARCHAR(MAX) NULL, `name_french` VARCHAR(MAX) NULL,`type` JSON NULL,`base_HP` INT NULL,`base_Attack` INT NULL,\
                                        `base_Defense` INT NULL,`base_Sp_Attack` INT NULL,`base_Sp_Defense` INT NULL,`base_Speed`INT NULL")
                    cur.execute("INSERT INTO data (id,name_english,name_japanese,name_chinese,name_french,type,base_HP,base_Attack,base_Defense,base_Sp_Attack,base_Sp_Defense,base_Speed) VALUES \
                                    (%d,%s,	%s,%s,%s,%s,%d,%d,%d,%d,%d,%d)", \
                                   (id, name_english, name_japanese, name_chinese, name_french, type, base_HP, base_Attack,
                                    base_Defense, base_Sp_Attack, base_Sp_Defense, base_Speed))
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.info('Database connection closed.')


Database(Config)