import json
from models.connection import Connection
from .exceptions import MissingAttributeException

MANIFEST_FILE = None

class ConnectionHandler():

    """"
    Handler for parsing the connection request descritpion in json 
    """

    def __init__(self,connection_data):
        super().__init__()
        self.connection = None

        self._id = None
        self._name = None
        self._ingress_port = None
        self._egress_port = None

    def import_connection_data(self, data):
        try:
            id = data['id']
            name=data['name']
            ingress_port=data['ingress_port']
            egress_port=data['elf._egress_port']
            quantity=data['quantity']
            start_time=data['start_time']
            end_time=data['end_time']
        except KeyError as e:
            raise MissingAttributeException(e.args[0],e.args[0])

        connection=Connection(id=id, name=name, domain_service = service, version=version, time_stamp=time_stamp, nodes=nodes, links=links)

        return connection

    def get_connection():
        return self.connection
