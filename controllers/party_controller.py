from models.party import Party
from repositories.party_repository import PartyRepository


class PartyController:

    def __init__(self):
        """
        Constructor of the PartyController class
        """
        self.party_repository = PartyRepository()

    def index(self) -> list:
        """
        Get all parties with the name and "lema"
        :return: list of dictionaries with all parties
        """
        return self.party_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        Get a specific party with de name and "lema"
        :param id_: party id
        :return: a dictionary of a particular party
        """
        return self.party_repository.find_by_id(id_)

    def create(self, party_: dict) -> dict:
        """
        Insert a new party
        :param party_: a dictionary carries the name and the party's "lema"
        :return: a dictionary with the information of the new party
        """
        party = Party(party_)
        return self.party_repository.save(party)

    def update(self, id_, party_: dict) -> dict:
        """
        Update a specific party
        :param id_: party id
        :param party_: a dictionary carries the name and the party's "lema"
        :return: a dictionary with a successful update
        """
        party = Party(party_)
        return self.party_repository.update(id_, party)

    def delete(self, id_: str) -> dict:
        """
        Delete a specific party
        :param id_: party id
        :return: a dictionary with a successful delete
        """
        return self.party_repository.delete(id_)
