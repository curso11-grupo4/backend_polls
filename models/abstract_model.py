from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        """
        This constructor method convert a dictionary in an object
        :param data: dictionary which is going to be parsed to a list of tuple
        """
        for key, value in data.items():
            setattr(self, key, value)
