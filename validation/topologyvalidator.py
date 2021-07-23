"""""
--------------------------------------------------------------------
Synopsis: A validation class to evaluate that the supplied Topology object contains expected data format
"""
from collections.abc import Iterable
from models import Topology, Node, Link, Location

ISO_FORMAT = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[-+]\d{2}:\d{2}'

class TopologyValidator:
    """
    The validation class made to validate a Topology
    """
    def __init__(self):
        self._topology = None
    @property
    def topology(self):
        return self._topology
    @topology.setter
    def topology(self, topology):
        if not isinstance(topology, Topology):
            raise ValueError('The Validator must be passed a Topology object')
        self._topology = topology
    @property
    def is_valid(self):
        errors = self.validate(self.topology, raise_error=False)
        for error in errors:
            print(error)
        return not bool(errors)
    def validate(self, topology=None, raise_error=True):
        if not topology and self.topology:
            topology = self.topology
        errors = self._validate_topology(topology)
        if errors and raise_error:
            raise ValueError('\n'.join(errors))
        return errors
    def _validate_topology(self, topology: Topology, parent=None):
        """
        Validate that the topology provided meets the JSON schema.
        A topology must have the following:
         - It must meet object default standards.
         - It must have a Primary owner assigned
         - It must have its primary owner in its institution list
         - It must have the global institution in the institution list
        :param topology: The topology being evaluated
        :param parent: The Parent Topology. If this topology is the top level, then the parent should be None.
        :return: A list of any issues in the data.
        """
        errors = []
        errors += self._validate_object_defaults(topology, parent)
        if not topology.primary_owner:
            errors.append('Topology {} ID: {} must have a primary owner'.format(topology.name, topology.id))
        elif topology.primary_owner not in topology.institutions:
            errors.append(
                'Topology {} ID: {} primary owner ID {} must be in the Topologies Institutions'.format(
                    topology.name, topology.id, topology.primary_owner,
                )
            )
        if not topology._parent == parent:
            errors.append(
                'Topology {} parent topology does not match. {} != {}'.format(
                    topology.id, topology._parent, parent
                )
            )
        if GLOBAL_INSTITUTION_ID not in topology.institutions:
            errors.append('Global Institution must be in Topology {}'.format(topology.id))
        for inst in topology.institutions:
            errors += self._validate_institution(inst, topology)
        for node in topology.nodes:
            errors += self._validate_node(node, topology)
        for link in topology.links:
            errors += self._validate_link(link, topology)
        for sub_topology in topology.topologies:
            errors += self._validate_topology(sub_topology, topology)
        return errors
    def _validate_institution(self, institution: Institution, topology: Topology):
        """
        Validate that the institution provided meets the XSD standards.
        A institution must have the following:
         - It must meet object default standards.
         - It's Location values are valid
         - The Institution Type must be in the list of valid Institution types
        :param institution: The Institution being evaluated.
        :param topology: The Parent Topology.
        :return: A list of any issues in the data.
        """
        errors = []
        errors += self._validate_object_defaults(institution, topology)
        errors += self._validate_location(institution, False)
        return errors
    def _validate_node(self, node: Node, topology: Topology):
        """
        Validate that the node provided meets the XSD standards.
        A node must have the following:
         - It must meet object default standards.
         - It's Location values are valid
         - It's Lifetime values are valid
         - All owners in the node must be strings
         - All owners in the node must be IDs for an institution in the parent topologies institution list
         - The node must have its parent Topology's primary owner in its list of owners
        :param node: The Node being evaluated.
        :param topology: The Parent Topology.
        :return: A list of any issues in the data.
        """
        errors = []
        errors += self._validate_object_defaults(node, topology)
        errors += self._validate_location(node)
        errors += self._validate_lifetime(node)
        for owner in node._owners:
            if not isinstance(owner, str):
                errors.append(
                    'Node {} owner {} should be a string. Not {}'.format(
                        node.id, owner, owner.__class__.__name__
                    )
                )
            if topology and owner not in topology.institutions:
                errors.append(
                    'Node {} listed owner id {} does not exist in parent Topology {}'.format(
                        node.id, owner, topology.id
                    )
                )
        if topology and topology.primary_owner not in node.owners:
            errors.append(
                'Node {} does not have the Topology primary owner {} in its list of owners'.format(
                    node.id, topology.primary_owner
                )
            )
        return errors
    def _validate_link(self, link: Link, topology: Topology):
        """
        Validate that the link provided meets the XSD standards.
        A link must have the following:
         - It must meet object default standards.
         - It's Lifetime values are valid
         - All owners in the link must be strings
         - All owners in the link must be IDs for an institution in the parent topologies institution list
         - The link must have its parent Topology's primary owner in its list of owners
         - A link can only connect to 2 nodes
         - The nodes that a link is connected to must be in the parent Topology's nodes list
        :param link: The Link being evaluated.
        :param topology: The Parent Topology.
        :return: A list of any issues in the data.
        """
        errors = []
        errors += self._validate_object_defaults(link, topology)
        errors += self._validate_lifetime(link)
        for owner in link._owners:
            if not isinstance(owner, str):
                errors.append(
                    'Link {} owner {} should be a string. Not {}'.format(
                        link.id, owner, owner.__class__.__name__
                    )
                )
            if topology and owner not in topology.institutions:
                errors.append(
                    'Link {} listed owner id {} does not exist in parent Topology {}'.format(
                        link.id, owner, topology.id
                    )
                )
        if topology and topology.primary_owner not in link.owners:
            errors.append(
                'Link {} does not have the Topology primary owner {} in its list of owners'.format(
                    link.id, topology.primary_owner
                )
            )
        if len(link._nodes) != 2:
            errors.append(
                'Link {} must connect between 2 Nodes. Currently {}'.format(
                    link.id, str(link._nodes)
                )
            )
        for node in link._nodes:
            if not isinstance(node, str):
                errors.append(
                    'Link {} Node {} should be a string. Not {}'.format(
                        link.id, node, node.__class__.__name__
                    )
                )
            if topology and node not in topology.nodes:
                errors.append(
                    'Link {} listed node id {} does not exist in parent Topology {}'.format(
                        link.id, node, topology.id
                    )
                )
        return errors