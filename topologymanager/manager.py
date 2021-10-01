
import json
import copy

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
        self.topology=None
        self.topology_list={}

    def get_handler(self):
        return self.handler

    def topology_id(self, id):  
        self.topology._id(id)
    
    def add_topology(self, data):

        topology = self.handler.import_topology_data(data)
        self.topology_list[topology.id] = topology

        if self.topology is None:
            self.topology = copy.deepcopy(topology)
            ##generate a new topology id
            self.generate_id()
        else:
            self.update_version(False)

        ## update the version and timestamp to be the latest
        ##check the inter-domain links first.
        self.inter_domain_check(topology)
        ##nodes
        nodes = topology.get_nodes()
        self.topology.add_nodes(nodes)
        ##links
        links = topology.get_links()
        self.topology.add_links(links)

        self.update_version(False)

    def generate_id(self):
        id=Topology.SDX_TOPOLOGY_ID_prefix
        self.topology.id(id)
        self.topology.version(Topology.TOPOLOGY_INITIAL_VERSION)
        return id
    
    def remove_topology(self, topology_id):
        self.topology_list.pop(topology_id, None)
        self.update_version(False)

    def update_topology(self,data):
        #likely adding new inter-domain links
        self.update_version(True)

    def get_topology(self):
        return self.topology

    def update_version(self,sub:bool):
        [ver, sub_ver] = self.topology.version.split('.')
        if not sub:
            ver=str(int(ver)+1)
        else:
            sub_ver=str(int(sub_ver)+1)

    def inter_domain_check(self,topology):
        interdomain_port_list=[]
        links = topology.get_links()
        for link in links:
            for port in link.ports:
                if port.inter_domain:
                    interdomain_port_list.append(port)

        #ToDo: raise an warning or exception
        if len(interdomain_port_list)==0:
            return False

        #match any ports in the existing topology
        for port in  interdomain_port_list:
            print("checking port:" + port.id)
            
        # remove the duplicated inter-domain links?
        # 
         
        return True

    def update_timestamp(self):
        pass

    def add_domain_service(self):
        pass

    def update_private_properties(self):
        pass

    def generate_grenml(self):
        pass