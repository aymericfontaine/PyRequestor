import unittest
from viewmodels.requestor_viewmodel import RequestorViewModel

class RequestorExecTestCase(unittest.TestCase):
    def setUp(self):
        self.vm = RequestorViewModel()


    def test_set_request_pos(self):
        self.vm.set_request_pos(2)
        self.assertEqual(self.vm.request_pos, 2)


    def test_set_param(self):
        self.vm.set_param(0, 'Hi')
        self.assertEqual(self.vm.params[0], 'Hi')


    # def test_exec_request(self)
