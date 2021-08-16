import json
from models.link import Link
from .exceptions import MissingAttributeException

class LinkHandler():

    """"
    Handler for parsing the connection request descritpion in json 
    """

    def __init__(self):
        super().__init__()
        self.link = None

    def import_link_data(self, data):
        try:
            id = data['id']
            name=data['name']
            short_name=data['short_name']
            ports=data['ports']
            timestamp=data['time_stamp']
            if 'total_bandwidth' in data.keys():
                t_b=data['total_bandwidth']
            a_b=data['available_bandwidth']
            latency=data['latency']
            p_l=data['packet_loss']
            p_a=data['private_attributes']
            avai=data['availability']
            m_p=data['measurement_period']
        except KeyError as e:
            raise MissingAttributeException(e.args[0],e.args[0])

        link=Link(id=id, name=name, short_name=short_name, ports=ports, total_bandwidth=t_b, available_bandwidth=a_b, 
            latency=latency, packet_loss=p_l, availability=avai, private_attributes=p_a, time_stamp=timestamp, measurement_period=None)

        return link
    
    def import_link(self,file):
        with open(file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            self.link = self.import_link_data(data)

    def get_link():
        return self.link
