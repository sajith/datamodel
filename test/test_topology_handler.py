import unittest

import parsing

from parsing.topologyhandler import TopologyHandler
from parsing.exceptions import DataModelException

TOPOLOGY_AMLIGHT = './test/amlight.json'

class TestTopologyHandler(unittest.TestCase):

    def setUp(self):
        self.handler = TopologyHandler(TOPOLOGY_AMLIGHT)  # noqa: E501

    def tearDown(self):
        pass

    def testImportTopology(self):
        try:
            print("Test")
            self.handler.import_topology()
            print(self.handler.topology)
        except DataModelException as e:
            print(e)
            return False
        return True

if __name__ == '__main__':
    unittest.main()