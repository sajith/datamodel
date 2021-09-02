
import json
from models.topology import Topology

import parsing
from parsing.topologyhandler import TopologyHandler
from parsing.exceptions import DataModelException

class TopologyManager():

    """"
    Manager for topology operations: merge multiple topologies, convert to grenml (XML).  
    """

    def __init__(self):
        super().__init__()

        self.handler = TopologyHandler()
        #self.topology=Topology() 

    def get_handler(self):
        return self.handler

    def topology_id(self, id):
        self.topology._id(id)
    
    def add_topology(self, data):
        topology = self.handler.import_topology_data(data)
        ##generate a new topology id
        ## update the version and timestamp to be the latest
        ##check the inter-domain links first.
        self.inter_domain_check(topology)
        ##nodes
        nodes = topology.get_nodes()
        self.topology.add_nodes(nodes)
        ##links
        links = topology.get_links()
        self.topology.add_links(nodes)

    def remove_topology(self, data):
        pass

    def update_topology(self,data):
        pass

    def get_topology():
        return self.topology

    def inter_domain_check(topology):
        pass


    def generate_grenml():
        pass