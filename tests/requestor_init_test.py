import unittest
from viewmodels.requestor_viewmodel import RequestorViewModel

class RequestorInitTestCase(unittest.TestCase):
    def setUp(self):
        self.vm = RequestorViewModel()


    def test_ini_db_host(self):
        self.assertNotEqual(self.vm.db.ini.db.host, '')
        self.assertNotEqual(self.vm.db.ini.table.request, '')
        self.assertNotEqual(self.vm.db.ini.table.requestparam, '')


    def test_ini_table_request(self):
        self.assertNotEqual(self.vm.db.ini.table.request, '')


    def test_ini_table_requestparam(self):
        self.assertNotEqual(self.vm.db.ini.table.requestparam, '')


    def test_requests(self):
        self.assertNotEqual(len(self.vm.requests), 0)


    def test_requestparams(self):
        a = 0
        for i in range(len(self.vm.requests)):
            a += len(self.vm.requests[i].params)

        self.assertNotEqual(a, 0)


    def test_request_pos(self):
        self.assertEqual(self.vm.request_pos, 0)