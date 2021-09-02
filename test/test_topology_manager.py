import unittest

import parsing
import topologymanager

from topologymanager.manager import TopologyManager
from topologymanager.grenmlconverter import GrenmlConverter
from parsing.exceptions import DataModelException


TOPOLOGY_AMLIGHT = './test/data/amlight.json'

class TestTopologyHandler(unittest.TestCase):

    def setUp(self):
        self.manager = TopologyManager()  # noqa: E501
        self.manager.handler.topology_file(TOPOLOGY_AMLIGHT)
        self.manager.handler.import_topology()

    def tearDown(self):
        pass

    def testMergeTopology(self):
        try:
            print("Test Topology")
            print(self.handler.topology)
        except DataModelException as e:
            print(e)
            return False      
        return True

    def testGrenmlConverter(self):
        try:
            print("Test Topology")
            print(self.handler.topology)
        except DataModelException as e:
            print(e)
            return False      
        return True