import unittest

import parsing

from parsing.nodehandler import NodeHandler
from parsing.exceptions import DataModelException

node = './test/data/node.json'

class TestNodeHandler(unittest.TestCase):

    def setUp(self):
        self.handler = NodeHandler()  # noqa: E501
    def tearDown(self):
        pass

    def testImportNode(self):
        try:
            print("Test node")
            self.handler.import_node(node)
            print(self.handler.node)
        except DataModelException as e:
            print(e)
            return False      
        return True

if __name__ == '__main__':
    unittest.main()