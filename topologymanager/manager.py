
import json
import copy

from models.topology import Topology, SDX_TOPOLOGY_ID_prefix,TOPOLOGY_INITIAL_VERSION
from models.link import Link
from models.port import Port


from parsing.topologyhandler import TopologyHandler
from parsing.exceptions import DataModelException

from .grenmlconverter import GrenmlConverter

class TopologyManager():

    """"
    Manager for topology operations: merge multiple topologies, convert to grenml (XML).  
    """

    def __init__(self):
        super().__init__()

        self.handler = TopologyHandler()

        self.topology=None
        self.topology_list={}
        self.port_list={} #{port, link}

        self.num_interdomain_link=0

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
            #Addding to the port list
            links = topology.get_links()
            for link in links:
                for port in link.ports:
                    self.port_list[port] = link
        else:
        ## update the version and timestamp to be the latest
            self.update_version(False)
            self.update_timestamp()

            ##check the inter-domain links first.
            self.num_interdomain_link+=self.inter_domain_check(topology)
            if self.num_interdomain_link==0:
                print("Warning: no interdomain links detected!")
            ##nodes
            nodes = topology.get_nodes()
            self.topology.add_nodes(nodes)
            ##links
            links = topology.get_links()
            self.topology.add_links(links)

            self.update_version(False)

    def generate_id(self):
        self.topology.set_id(SDX_TOPOLOGY_ID_prefix)
        self.topology.set_version(TOPOLOGY_INITIAL_VERSION)
        return id
    
    def remove_topology(self, topology_id):
        self.topology_list.pop(topology_id, None)
        self.update_version(False)
        self.update_timestamp()

    def update_topology(self,data):
        #likely adding new inter-domain links
        topology = self.handler.import_topology_data(data)
        self.topology_list[topology.id] = topology

        ##nodes
        nodes = topology.get_nodes()
        for node in nodes:
            self.topology.remove_node(node.id)
        ##links
        links = topology.get_links()
        for link in links:
            self.topology.remove_links(link.id)

        ##check the inter-domain links first.
        num_interdomain_link=self.inter_domain_check(topology)
        if num_interdomain_link==0:
            print("Warning: no interdomain links detected!")

        ##nodes
        nodes = topology.get_nodes()
        self.topology.add_nodes(nodes)
        ##links
        links = topology.get_links()
        self.topology.add_links(links)

        self.update_version(True)
        self.update_timestamp()

    def get_topology(self):
        return self.topology

    def update_version(self,sub:bool):
        [ver, sub_ver] = self.topology.version.split('.')
        if not sub:
            ver=str(int(ver)+1)
        else:
            sub_ver=str(int(sub_ver)+1)

    def inter_domain_check(self,topology):
        interdomain_port_dict={}
        num_interdomain_link=0
        links = topology.get_links()
        link_dict ={}
        for link in links:
            link_dict[link.id] = link
            for port in link.ports:
                    interdomain_port_dict[port]=link

        #ToDo: raise an warning or exception
        if len(interdomain_port_dict)==0:
            return False

        #match any ports in the existing topology
        for port_id in  interdomain_port_dict:
            print("checking port:" + port_id)
            for existing_port, existing_link in self.port_list.items():
                if port_id == existing_port:
                    #remove redundant link between two domains
                    self.topology.remove_link(existing_link.id)   
                    num_interdomain_link=+1     

        return num_interdomain_link

    def update_timestamp(self):
        pass

    def add_domain_service(self):
        pass

    def update_private_properties(self):
        pass

    def generate_graph(self):
        pass

    def generate_grenml(self):
        self.converter = GrenmlConverter(self.topology)

        return self.converter.read_topology()    