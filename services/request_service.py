from db.db import Db, DbType
from models.request_model import RequestModel

class RequestServiceResult:
    sql: str
    columns: list[str]
    results: list[str]


class RequestService:
    def __init__(self, db: Db):
        self.db = db
        self.select = "SELECT * FROM " + self.db.ini.table.request

    # Get all requests
    def getall(self) -> list[RequestModel]:
        if self.db.ini.db.type == DbType.DB2.value:
            return self.__getall_db2()
        elif self.db.ini.db.type == DbType.MYSQL.value:
            return self.__getall_mysql()
        else:
            raise


    # Get single request
    def getsingle(self, id: int) -> list[RequestModel]:
        if self.db.ini.db.type == DbType.DB2.value:
            return self.__getsingle_db2(id)
        elif self.db.ini.db.type == DbType.MYSQL.value:
            return self.__getsingle_mysql(id)
        else:
            raise


    # Get all requests DB2
    def __getall_db2(self)-> list[RequestModel]:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select)
        rows = cursor.fetchall()
        cursor.close()

        requests = []
        for row in rows:
            request = RequestModel()
            request.id = row[0]
            request.num = row[1]
            request.label = row[2]
            request.req = row[3]
            
            requests.append(request)

        return requests


    # Get all requests MYSQL
    def __getall_mysql(self)-> list[RequestModel]:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select)
        rows = cursor.fetchall()
        cursor.close()

        requests = []
        for row in rows:
            request = RequestModel()
            request.id = row[0]
            request.num = row[1]
            request.label = row[2]
            request.req = row[3]

            requests.append(request)

        return requests


    # Get single request DB2
    def __getsingle_db2(self, id: int)-> RequestModel:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select + ' WHERE ID = ' + id)
        row = cursor.fetchone()
        cursor.close()

        request = RequestModel()
        request.id = row[0]
        request.num = row[1]
        request.label = row[2]
        request.req = row[3]

        return request


    # Get single request MYSQL
    def __getsingle_mysql(self, id: int)-> list[RequestModel]:
        cursor = self.db.cnx.cursor()
        cursor.execute(self.select + ' WHERE ID = ' + id)
        row = cursor.fetchone()
        cursor.close()

        request = RequestModel()
        request.id = row[0]
        request.num = row[1]
        request.label = row[2]
        request.req = row[3]

        return request


    # Get result
    def getresult(self, request: RequestModel, params: dict) -> RequestServiceResult:
        sql = request.req
        
        for key in params:
            sql = sql.replace("{" + str(key) + "}",  params[key].replace("'","''"))

        if self.db.ini.db.type == DbType.DB2.value:
            return self.__getresult_db2(sql)
        elif self.db.ini.db.type == DbType.MYSQL.value:
            return self.__getresult_mysql(sql)
        else:
            raise


    # Get result DB2
    def __getresult_db2(self, sql: str) -> RequestServiceResult:
        cursor = self.db.cnx.cursor()
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        results = cursor.fetchall()
        cursor.close()

        result = RequestServiceResult()
        result.sql = sql
        result.columns = columns
        result.results = results

        return result
        

    # Get result MYSQL
    def __getresult_mysql(self, sql: str) -> RequestServiceResult:
        cursor = self.db.cnx.cursor()
        cursor.execute(sql)
        columns = cursor.column_names
        results = cursor.fetchall()
        cursor.close()

        result = RequestServiceResult()
        result.sql = sql
        result.columns = columns
        result.results = results

        return result
