import json
from models.service import Service
from .exceptions import MissingAttributeException

class ServiceHandler():

    """"
    Handler for parsing the connection request descritpion in json 
    """

    def __init__(self):
        super().__init__()
        self.service = None

    def import_service_data(self, data):
        try:
            id = data['id']
            name=data['name']
            start=data['start_time']
            end=data['end_time']
            ingress=data['ingress_port']
            egress=data['egress_port']
        except KeyError as e:
            raise MissingAttributeException(e.args[0],e.args[0])

        service=Service(id=id, name=name, start_time = start, end_time = end, ingress_port = ingress, egress_port = egress)

        return service
    
    def import_service(self,file):
        with open(file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            self.service = self.import_service_data(data)

    def get_service():
        return self.service
