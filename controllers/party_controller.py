from models.party import Party
from repositories.party_repository import PartyRepository


class PartyController:

    def __init__(self):
        print("Party controller ready...")
        self.party_repository = PartyRepository

    def index(self) -> list:
        """
        Get all paries with the name and "lema"
        :return:
        """
        print("Get all parties")
        return self.party_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        Get a specific party with de name and "lema"
        :param id_: party id
        :return:
        """
        print("Get one party")
        return self.party_repository.find_by_id(id_)

    def create(self, party_: dict) -> dict:
        """
        Insert a new party
        :param party_: a dictionary carries the name a "lema"
        :return:
        """
        print("Insert one party")
        party = Party(party_)
        return self.party_repository.save(party)

    def update(self, id_, party_: dict) -> dict:
        """
        Update a specific party
        :param id_:
        :param party_:
        :return:
        """
        print("Update one party")
        party = Party(party_)
        return self.party_repository.update(id_, party)

    def delete(self, id_: str) -> dict:
        """
        Delete a specific party
        :param id_: party id
        :return:
        """
        print("Delete one party")
        return self.party_repository.delete(id_)
