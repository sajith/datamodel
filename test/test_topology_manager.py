import unittest
import json
from networkx import MultiGraph, Graph
import matplotlib.pyplot as plt
import networkx as nx

from sdxdatamodel import parsing
from sdxdatamodel import topologymanager

from sdxdatamodel import validation
from sdxdatamodel.validation.topologyvalidator import TopologyValidator
from sdxdatamodel.parsing.topologyhandler import TopologyHandler
from sdxdatamodel.topologymanager.manager import TopologyManager
from sdxdatamodel.topologymanager.grenmlconverter import GrenmlConverter
from sdxdatamodel.parsing.exceptions import DataModelException


TOPOLOGY_AMLIGHT = './test/data/amlight.json'
TOPOLOGY_SAX = './test/data/sax.json'
TOPOLOGY_ZAOXI = './test/data/zaoxi.json'

topology_file_list_3 = [TOPOLOGY_AMLIGHT,TOPOLOGY_SAX, TOPOLOGY_ZAOXI]
topology_file_list_2 = [TOPOLOGY_SAX, TOPOLOGY_ZAOXI]

class TestTopologyManager(unittest.TestCase):

    def setUp(self):
        self.manager = TopologyManager()  # noqa: E501

    def tearDown(self):
        pass

    def testMergeTopology(self):
        print("Test Topology Merge!")
        try:
            for topology_file in topology_file_list_3:
                with open(topology_file, 'r', encoding='utf-8') as data_file:
                    data = json.load(data_file)
                print("Adding Topology:" + topology_file)
                self.manager.add_topology(data)
            
        except DataModelException as e:
            print(e)
            return False      
        return True

    def testGrenmlConverter(self):
        try:
            print("Test Topology GRENML Converter")
            self.testMergeTopology()
            converter = GrenmlConverter(self.manager.get_topology())
            converter.read_topology()
            print(converter.get_xml_str)
        except DataModelException as e:
            print(e)
            return False      
        return True

    def testGenerateGraph(self):
        try:
            print("Test Topology Graph")
            self.testMergeTopology()
            graph = self.manager.generate_graph()
            #pos = nx.spring_layout(graph, seed=225)  # Seed for reproducible layout
            nx.draw(graph,with_labels = True)
            plt.savefig("./test/data/amlight.png")
        except DataModelException as e:
            print(e)
            return False      
        return True

if __name__ == '__main__':
    unittest.main()