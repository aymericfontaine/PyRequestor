import sys
from viewmodels.requestor_viewmodel import RequestorViewModel
from PyQt5.QtWidgets import QApplication, QComboBox, QFileDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class Desktop(QWidget):
    def __init__(self):
        super().__init__()

        self.vm = RequestorViewModel()
        
        self.layout = QVBoxLayout()

        self.layout_requests = QGridLayout()
        self.layout_params = QGridLayout()
        self.layout_result = QGridLayout()

        self.lbl_requests = QLabel('Request')
        self.cb_requests = QComboBox()

        self.params = dict()

        self.btn_execute = QPushButton('Execute')
        self.btn_execute.clicked.connect(self.execute)

        self.table_result = QTableWidget()

        self.btn_excel = QPushButton('Excel')
        self.btn_excel.clicked.connect(self.export_excel)


    def lanchapp(self):
        self.cb_requests.currentIndexChanged.connect(self.change_request)
        for request in self.vm.requests:
            self.cb_requests.addItem(request.label)

        self.display_params()
        self.display_result()

        self.layout_requests.addWidget(self.lbl_requests, 0, 1)
        self.layout_requests.addWidget(self.cb_requests, 0, 2)

        self.layout_result.addWidget(self.btn_execute, 0, 2)
        self.layout_result.addWidget(self.table_result, 1, 1, 1, 2)
        self.layout_result.addWidget(self.btn_excel, 2, 2)

        self.layout.addLayout(self.layout_requests)
        self.layout.addLayout(self.layout_params)
        self.layout.addLayout(self.layout_result)

        self.setLayout(self.layout)
        self.setGeometry(250, 250, 1000, 750)
        self.show()


    def display_params(self):
        # Clear params list and layout
        for i in reversed(range(len(self.params))): 
            self.layout_params.removeWidget(self.params[i][0])
            self.layout_params.removeWidget(self.params[i][1])
            self.params[i][0].deleteLater()
            self.params[i][1].deleteLater()
            del self.params[i]

        self.params = dict()

        for i in range(len(self.vm.requests[self.vm.request_pos].params)):
            lbl_param = QLabel()
            lbl_param.setText(self.vm.requests[self.vm.request_pos].params[i].label)

            txt_param = QLineEdit()
            txt_param.setPlaceholderText(self.vm.requests[self.vm.request_pos].params[i].help)
           
            self.params[i] = [lbl_param, txt_param]
            self.layout_params.addWidget(lbl_param, i, 1)
            self.layout_params.addWidget(txt_param, i, 2)


    def display_result(self):
        self.table_result.setRowCount(len(self.vm.results)) 
        self.table_result.setColumnCount(len(self.vm.columns))  
        self.table_result.setHorizontalHeaderLabels(self.vm.columns)

        for i in range(len(self.vm.results)):
            for j in range(len(self.vm.results[i])):
                self.table_result.setItem(i, j, QTableWidgetItem(str(self.vm.results[i][j])))


    def change_request(self, i):
        self.vm.set_request_pos(i)
        self.display_params()


    def execute(self):
        for i in range(len(self.params)):
            txt_param = self.layout_params.itemAtPosition(i, 2).widget()
            self.vm.set_param(i,txt_param.text())

        self.vm.exec_request()
        self.display_result()


    def export_excel(self):
        file = QFileDialog.getSaveFileName(self, 'Save file')
        if file != '':
            self.vm.export_excel(file[0])


app = QApplication(sys.argv)
desktop = Desktop()
desktop.lanchapp()
sys.exit(app.exec_())