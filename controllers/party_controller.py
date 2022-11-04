

class PartyController:

    def __init__(self):
        print("Party controller ready...")

    def index(self) -> list:
        """
        Get all paries with the name and "lema"
        :return:
        """
        print("Get all parties")

    def show(self, _id: str) -> dict:
        """
        Get a specific party with de name and "lema"
        :param _id: party id
        :return:
        """
        print("Get one party")

    def create(self, party: dict) -> dict:
        """
        Insert a new party
        :param party: a dictionary carries the name a "lema"
        :return:
        """
        print("Insert one party")

    def update(self, _id, party: dict) -> dict:
        """
        Update a specific party
        :param _id:
        :param party:
        :return:
        """
        print("Update one party")

    def delete(self, _id):
        """
        Delete a specific party
        :param _id: party id
        :return:
        """
        print("Delete one party")

