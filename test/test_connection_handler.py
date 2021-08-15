import unittest

import parsing

from parsing.connectionhandler import ConnectionHandler
from parsing.exceptions import DataModelException

CONNECTION_P2P = './test/p2p.json'

class TestConnectionHandler(unittest.TestCase):

    def setUp(self):
        self.handler = ConnectionHandler(CONNECTION_P2P)  # noqa: E501
    def tearDown(self):
        pass

    def testImportConnection(self):
        try:
            print("Test Connection")
            self.handler.import_connection(CONNECTION_P2P)
            print(self.handler.connection)
        except DataModelException as e:
            print(e)
            return False      
        return True

if __name__ == '__main__':
    unittest.main()