# coding: utf-8

"""
    SDX LC

    You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
import six

from parsing.servicehandler import ServiceHandler
from parsing.nodehandler import NodeHandler
from parsing.linkhandler import LinkHandler

SDX_INSTITUTION_ID = 'urn:ogf:network:sdx'
SDX_TOPOLOGY_ID_prefix = "urn:ogf:network:sdx"
TOPOLOGY_INITIAL_VERSION="0.0"

class Topology(object):

    swagger_types = {
        'id': 'str',
        'name': 'str',
        'domain_service': 'Service',
        'version': 'int',
        'time_stamp': 'datetime',
        'nodes': 'list[Node]',
        'links': 'list[Link]',
        'private_attributes': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain_service': 'domain_service',
        'version': 'version',
        'time_stamp': 'time_stamp',
        'nodes': 'nodes',
        'links': 'links',
        'private_attributes': 'private_attributes'
    }

    def __init__(self, id=None, name=None, domain_service=None, version=None, time_stamp=None, nodes=None, links=None, private_attributes=None):  # noqa: E501
        """Topology - a model defined in Swagger"""  # noqa: E501

        self._domain_service = None
        self._private_attributes = None
        self._id = id
        self._name = name
        if domain_service is not None:
            self._domain_service = self.set_domain_service(domain_service)
        self._version = version
        self._time_stamp = time_stamp
        self._nodes=[]
        self._links=[]
        self._nodes = self.set_nodes(nodes)
        self._links = self.set_links(links)
        if private_attributes is not None:
            self._private_attributes = private_attributes

    @property
    def id(self):
        """Gets the id of this Topology.  # noqa: E501


        :return: The id of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Topology.


        :param id: The id of this Topology.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Topology.  # noqa: E501


        :return: The name of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Topology.


        :param name: The name of this Topology.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain_service(self):
        """Gets the name of this Topology.  # noqa: E501


        :return: The name of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._domain_service

    def get_domain_service(self):
        """Gets the domain_service of this Topology.  # noqa: E501


        :return: The domain_service of this Topology.  # noqa: E501
        :rtype: Service
        """
        return self._domain_service

    def set_domain_service(self, domain_service):
        """Sets the domain_service of this Topology.


        :param domain_service: The domain_service of this Topology.  # noqa: E501
        :type: Service
        """
        if domain_service is None:
            raise ValueError("Invalid value for `domain_service`, must not be `None`")  # noqa: E501

        service_handler = ServiceHandler()
        self._domain_service = service_handler.import_service_data(domain_service)
        
        return self.get_domain_service()


    @property
    def version(self):
        """Gets the version of this Topology.  # noqa: E501


        :return: The version of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Topology.


        :param version: The version of this Topology.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def time_stamp(self):
        """Gets the time_stamp of this Topology.  # noqa: E501


        :return: The time_stamp of this Topology.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this Topology.


        :param time_stamp: The time_stamp of this Topology.  # noqa: E501
        :type: datetime
        """
        if time_stamp is None:
            raise ValueError("Invalid value for `time_stamp`, must not be `None`")  # noqa: E501

        self._time_stamp = time_stamp

    @property
    def nodes(self):
        """Gets the name of this Topology.  # noqa: E501


        :return: The name of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._nodes

    def get_nodes(self):
        """Gets the nodes of this Topology.  # noqa: E501


        :return: The nodes of this Topology.  # noqa: E501
        :rtype: list[Node]
        """
        return self._nodes

    def set_nodes(self, nodes):
        """Sets the nodes of this Topology.


        :param nodes: The nodes of this Topology.  # noqa: E501
        :type: list[Node]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        for node in nodes:
            node_handler = NodeHandler()
            node_obj = node_handler.import_node_data(node)
            self._nodes.append(node_obj)
        
        return self.get_nodes()

    def add_nodes(self, node_objects):
        """add the nodes to this Topology.
        :param node_objects: a list of node objects
        """

        self._nodes.extend(node_objects)

    def get_node_by_port(self,aPort):
        for node in self.nodes:
            ports = node.ports
            for port in ports:
                if port.id == aPort['id']:
                    return node
        
        return None


    @property
    def links(self):
        """Gets the name of this Topology.  # noqa: E501


        :return: The name of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._links

    def get_links(self):
        """Gets the links of this Topology.  # noqa: E501


        :return: The links of this Topology.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    def set_links(self, links):
        """Sets the links of this Topology.

        :param links: The links of this Topology, in list of JSON str.  # noqa: E501
        :type: list[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        for link in links:
            link_handler = LinkHandler()
            link_obj = link_handler.import_link_data(link)
            self._links.append(link_obj)
        
        return self.get_links()

    def add_links(self, link_objects):
        """add the links to this Topology.
        :param link_objects: a list of link objects
        """

        self._nodes.extend(link_objects)

    @property
    def private_attributes(self):
        """Gets the private_attributes of this Topology.  # noqa: E501


        :return: The private_attributes of this Topology.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_attributes

    @private_attributes.setter
    def private_attributes(self, private_attributes):
        """Sets the private_attributes of this Topology.


        :param private_attributes: The private_attributes of this Topology.  # noqa: E501
        :type: list[str]
        """

        self._private_attributes = private_attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Topology, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Topology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
