from enum import Enum
from models.ini import Ini
import pyodbc
import mysql.connector

class Db:
    def __init__(self):
        self.ini: Ini
        self.cnx = None

    def connect(self,ini: Ini):
        self.ini = ini

        if self.ini.db.type == DbType.DB2.value:
            self.cnx = pyodbc.connect(driver = '{iSeries Access ODBC Driver}', system = self.ini.db.host, uid = self.ini.db.user, pwd = self.ini.db.password)

        elif self.ini.db.type == DbType.MYSQL.value:
            self.cnx = mysql.connector.connect(user = self.ini.db.user, password = self.ini.db.password, host = self.ini.db.host, database = self.ini.db.database)

        else:
            raise


class DbType(Enum):
    DB2 = 'DB2'
    MYSQL = 'MYSQL'
