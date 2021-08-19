import unittest

import parsing

from validation.topologyvalidator import TopologyValidator
from parsing.topologyhandler import TopologyHandler
from parsing.exceptions import DataModelException

TOPOLOGY_AMLIGHT = './test/data/amlight.json'

class TestTopologyValidator(unittest.TestCase):

    def setUp(self):
        self.handler = TopologyHandler(TOPOLOGY_AMLIGHT)
        self.validator = TopologyValidator()  

    def tearDown(self):
        pass

    def testTopology(self):
        try:
            print("Import Topology:")
            self.handler.import_topology()
            self.validator.set_topology(self.handler.topology)
            self.validator.is_valid()
            print(self.handler.topology)
        except DataModelException as e:
            print(e)
            return False
        return True

if __name__ == '__main__':
    unittest.main()