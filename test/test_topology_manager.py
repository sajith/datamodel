import unittest
import json

import parsing
import topologymanager

from validation.topologyvalidator import TopologyValidator
from parsing.topologyhandler import TopologyHandler
from topologymanager.manager import TopologyManager
from topologymanager.grenmlconverter import GrenmlConverter
from parsing.exceptions import DataModelException


TOPOLOGY_AMLIGHT = './test/data/amlight.json'
TOPOLOGY_SAX = './test/data/sax.json'
TOPOLOGY_ZHAOXI = './test/data/zhaoxi.json'

topology_file_list = [TOPOLOGY_AMLIGHT,TOPOLOGY_SAX, TOPOLOGY_ZHAOXI]

class TestTopologyManager(unittest.TestCase):

    def setUp(self):
        self.manager = TopologyManager()  # noqa: E501

    def tearDown(self):
        pass

    def testMergeTopology(self):
        print("Test Topology Merge!")
        try:
            for topology_file in topology_file_list:
                with open(self.topology_file, 'r', encoding='utf-8') as data_file:
                    data = json.load(data_file)
                print("Adding Topology:" + topology_file)
                self.manager.add_topology(self, data)
            
        except DataModelException as e:
            print(e)
            return False      
        return True

    def testGrenmlConverter(self):
        try:
            print("Test Topology GRENML Converter")
            converter = GrenmlConverter(self.topology)
            converter.read_topology()
            print(converter.get_xml_str)
        except DataModelException as e:
            print(e)
            return False      
        return True