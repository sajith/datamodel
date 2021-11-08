class DataModelException(Exception):
    """
    Base exception for GRENML parsing
    """
    pass

class MissingAttributeException(DataModelException):
    """
    A required attribute could not be found when parsing an element
    """

    def __init__(self, attribute_name, expected_attribute):
        self.attribute_name = attribute_name
        self.expected_attribute = expected_attribute

    def __str__(self):
        return ("Missing attribute {} while parsing <{}>").format(
            self.expected_attribute,
            self.attribute_name,
        )



