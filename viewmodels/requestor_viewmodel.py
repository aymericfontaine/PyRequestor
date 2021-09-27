from models.ini import Ini
from models.requestparam_model import RequestParamModel
import xlsxwriter
import copy
from db.db import Db, DbType
from services.request_service import RequestService
from services.requestparam_service import RequestParamService

class RequestorViewModel:
    def __init__(self):
        self.ini = Ini()
        
        self.db = Db()
        self.db.connect(self.ini)

        self.request_service = RequestService(self.db)
        self.requestparam_service = RequestParamService(self.db)
        
        self.requests = []
        self.request_pos = -1

        self.params = dict()

        self.sql: str
        self.columns = []
        self.results = []

        self.init_requests()


    def init_requests(self):
        self.requests = self.request_service.getall()
        self.requests.sort(key=lambda x: x.num)

        requestparams = self.requestparam_service.getall()
        requestparams.sort(key=lambda x: x.num)

        for i in range(len(self.requests)):
            self.requests[i].params = []
            for j in range(len(requestparams)):
                if self.requests[i].id == requestparams[j].idrequest:
                    self.requests[i].params.append(copy.copy(requestparams[j]))

        if len(self.requests) == 0:
            self.set_request_pos(-1)
        else:
            self.set_request_pos(0)

        
    def set_request_pos(self, pos: int):
        self.request_pos = pos
        self.params = dict()


    def set_param(self, key: int, value):
        self.params[key] = value


    def exec_request(self):
        result = self.request_service.getresult(self.requests[self.request_pos],self.params)
        self.sql = result.sql
        self.columns = result.columns
        self.results = result.results


    def export_excel(self, file: str):
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()

        for i in range(len(self.columns)):
            worksheet.write(0, i, self.columns[i])

        for i in range(len(self.results)):
            row = i + 1
            for j in range(len(self.results[i])):
                worksheet.write(row, j, self.results[i][j])
        
        workbook.close()