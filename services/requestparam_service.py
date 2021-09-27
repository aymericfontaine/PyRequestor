from db.db import Db, DbType
from models.requestparam_model import RequestParamModel

class RequestParamService:
    def __init__(self, db: Db):
        self.db = db

        self.select = "SELECT * FROM " + self.db.ini.table.requestparam


    # Get all parameters
    def getall(self) -> list[RequestParamModel]:
        if self.db.ini.db.type == DbType.DB2.value:
            return self.__getall_db2()
        elif self.db.ini.db.type == DbType.MYSQL.value:
            return self.__getall_mysql()
        else:
            raise


    # Get single parameter
    def getsingle(self, id: int) -> list[RequestParamModel]:
        if self.db.ini.db.type == DbType.DB2.value:
            return self.__getsingle_db2(id)
        elif self.db.ini.db.type == DbType.MYSQL.value:
            return self.__getsingle_mysql(id)
        else:
            raise


    # Get all parameters DB2
    def __getall_db2(self)-> list[RequestParamModel]:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select)
        rows = cursor.fetchall()
        cursor.close()

        requests = []
        for row in rows:
            request = RequestParamModel()
            request.id = row[0]
            request.idrequest = row[1]
            request.num = row[2]
            request.label = row[3]
            request.help = row[4]

            requests.append(request)

        return requests


    # Get all parameters MYSQL
    def __getall_mysql(self)-> list[RequestParamModel]:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select)
        rows = cursor.fetchall()
        cursor.close()

        requests = []
        for row in rows:
            request = RequestParamModel()
            request.id = row[0]
            request.idrequest = row[1]
            request.num = row[2]
            request.label = row[3]
            request.help = row[4]

            requests.append(request)

        return requests


    # Get single parameter DB2
    def __getsingle_db2(self, id: int)-> RequestParamModel:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select + ' WHERE ID = ' + id)
        row = cursor.fetchone()
        cursor.close()

        request = RequestParamModel()
        request.id = row[0]
        request.idrequest = row[1]
        request.num = row[2]
        request.label = row[3]
        request.help = row[4]

        return request


    # Get single parameter MYSQL
    def __getsingle_mysql(self, id: int)-> list[RequestParamModel]:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select + ' WHERE ID = ' + id)
        row = cursor.fetchone()
        cursor.close()

        request = RequestParamModel()
        request.id = row[0]
        request.idrequest = row[1]
        request.num = row[2]
        request.label = row[3]
        request.help = row[4]
        
        return request