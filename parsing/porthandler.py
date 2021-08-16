import json
from models.port import Port
from .exceptions import MissingAttributeException

class PortHandler():

    """"
    Handler for parsing the connection request descritpion in json 
    """

    def __init__(self):
        super().__init__()
        self.port = None

    def import_port_data(self, data):
        try:
            id = data['id']
            name=data['name']
            short_name=data['short_name']
            node=data['node']
            l_r=None
            if 'label_range' in data.keys():  
                l_r=data['label_range']
            p_a=None
            if 'private_attributes' in data.keys():     
                p_a=data['private_attributes']
        except KeyError as e:
            raise MissingAttributeException(e.args[0],e.args[0])

        port=Port(id=id, name=name,short_name=short_name, node=node, label_range=l_r, status=None, private_attributes=p_a)

        return port
    
    def import_port(self,file):
        with open(file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            self.port = self.import_port_data(data)

    def get_port():
        return self.port
