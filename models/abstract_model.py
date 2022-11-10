from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        """
        Este método constructo convierte un diccionario en un objeto
        :param data:
        :return:
        """
        for key, value in data.items():
            setattr(self, key, value)
