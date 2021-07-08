from models import topology


class TopologyHandler():

    """"
    Handler for parsing the topology descritpion in json 
    """

    import json
    from datamodel.models.topology import Topology
    from .exception import MissingAttributeException

    def __init__(self):
        super().__init__()
        self.topology_file=MANIFEST_FILE=None
        self.topology = None

    def _import_topology(self, topology_filename):
        with open(topology_filename) as data_file:
            data = json.load(data_file)

        try:
            id = data['id']
            name=data['name']
            version=data['version']
            time_stamp=data['time_stamp']
            nodes=data['nodes']
            links=data['links']
        except:
            raise MissingAttributeException()

        topology=Topology(id=id, name=name, version=version, time_stamp=time_stamp, nodes=nodes, links=links)
        
    def get_topology():
        return self.topology
