import grenml

from models.topology import Topology
from models.node import Node
from models.location import Location

class GrenmlConverter(object):

    def __init__(self, topology:Topology):
        self.topology=topology
        self.grenml_manager = grenml.GRENMLManager(topology.name())

    def read_topology(self):
        domain_service = self.topology.get_domain_service()
        owner = domain_service._owner
        self.grenml_manager.set_primary_owner(owner)

        self.grenml_manager.add_institution(owner)

        self.add_nodes(self.topology.get_nodes())

        self.add_links(self.topology.get_links())

        self.topology_str = self.grenml_manager.write_to_string()

    def add_nodes(self,nodes):
        for node in nodes:
            location = node.get_location()
            self.grenml_manager.add_node(node.id, node.name,node.short_name,longitude=location.longitude,latitude=location.latitude, address=location.address())

    def add_links(self,links):
        for link in links:
            ports=link.ports
            end_nodes=[]
            for port in ports:
                node=self.topology.find_node_by_port(port)
                if node is not None:
                    end_nodes.append(node)
                else:
                    print("This port doesn't belong to any node in the topology!")

            self.grenml_manager.add_link(link.id, link.name,link.short_name, nodes=end_nodes)

    def get_xml_str(self):
        return self.topology_str