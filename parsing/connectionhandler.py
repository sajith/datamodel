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
            start=data['start_time']
            end=data['end_time']
            ingress=data['ingress_port']
            egress=data['egress_port']
        except KeyError as e:
            raise MissingAttributeException(e.args[0],e.args[0])

        connection=Connection(id=id, name=name, start_time = start, end_time = end, ingress_port = ingress, egress_port = egress)

        return connection
    
    def import_connection(self,file):
        with open(file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            self.connection = self.import_connection_data(data)

    def get_connection():
        return self.connection
