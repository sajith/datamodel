
import json
import copy

import networkx as nx

from sdxdatamodel.models.topology import Topology, SDX_TOPOLOGY_ID_prefix,TOPOLOGY_INITIAL_VERSION
from sdxdatamodel.models.link import Link
from sdxdatamodel.models.port import Port
from sdxdatamodel.models.connection import Connection

from sdxdatamodel.parsing.connectionhandler import ConnectionHandler
from sdxdatamodel.topologymanager.manager import TopologyManager
from sdxdatamodel.parsing.topologyhandler import TopologyHandler
from sdxdatamodel.parsing.exceptions import DataModelException

from .manager import TopologyManager

class TEManager():

    """"
    TE Manager for connection - topology operations: (1) generate inputs to the PCE solver; (2) converter the solver output.  
    """


    def __init__(self, topology_data, connection_data):
        super().__init__()

        self.manager = TopologyManager()
        self.connection_handler = ConnectionHandler()

        self.manager.topology = self.manager.get_handler().import_topology_data(topology_data)
        self.connection = self.connection_handler.import_connection_data(connection_data)

        self.graph = self.generate_graph_te()

    def generate_connection_te(self):
        ingress_port = self.connection.ingress_port
        ingress_node = self.manager.topology.get_node_by_port(ingress_port.id)
        egress_port = self.connection.egress_port
        egress_node = self.manager.topology.get_node_by_port(egress_port.id)

        i_node = [x for x,y in self.graph.nodes(data=True) if y['name']==ingress_node.name]
        e_node = [x for x,y in self.graph.nodes(data=True) if y['name']==egress_node.name]

        bandwidth_required=self.connection.bandwidth
        latency_required=self.connection.latency
        requests=[]
        request=[i_node[0],e_node[0],bandwidth_required,latency_required]
        requests.append(request)

        return requests

    def generate_graph_te(self):
        graph = self.manager.generate_graph()
        graph = nx.convert_node_labels_to_integers(graph,label_attribute='name')
        return graph
