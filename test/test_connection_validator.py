import unittest

import parsing

from validation.connectionvalidator import ConnectionValidator
from parsing.connectionhandler import ConnectionHandler
from parsing.exceptions import DataModelException

CONNECTION_P2P = './test/p2p.json'

class TestConnectionValidator(unittest.TestCase):

    def setUp(self):
        self.handler = ConnectionHandler()
        print("Import Connection:")
        self.handler.import_connection(CONNECTION_P2P)
        conn = self.handler.connection
        self.validator = ConnectionValidator() 
        self.validator.set_connection(conn)

    def tearDown(self):
        pass

    def testConnection(self):
        try:
            self.validator.is_valid()
            print(self.validator.get_connection())
        except DataModelException as e:
            print(e)
            return False
        return True

if __name__ == '__main__':
    unittest.main()