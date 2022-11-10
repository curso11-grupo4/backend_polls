from models.candidate import Candidate
from models.party import Party
from repositories.candidate_repository import CandidateRepository
from repositories.party_repository import PartyRepository


class CandidateController:

    def __init__(self):
        print("Candidate controller ready...")
        self.candidate_repository = CandidateRepository()
        self.party_repository = PartyRepository()

    def index(self) -> list:
        """
        Get all candidate with number of resolution, personal_id, name and lastname
        :return:
        """
        print("Get all candidate")
        return self.candidate_repository.find_all()

    def show(self, personal_id_: str) -> dict:
        """
        Get a specific candidate with the personal id
        :param personal_id_:
        :return:
        """
        print("Get a candidate")
        return self.candidate_repository.find_by_id(personal_id_)

    def create(self, candidate_: dict) -> dict:
        """
        Insert a new candidate
        :param candidate_: a dictionary carries personal id, resolution number, name and lastname
        :return:
        """
        print("Insert a new candidate")
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, personal_id_: str, candidate_: dict) ->dict:
        """
        Update a specific candidate
        :param personal_id_: candidate's personal_id
        :param candidate_: a dictionary with resolution number, name and lastname
        :return:
        """
        print("Update a candidate")
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(personal_id_, candidate)

    def delete(self, personal_id_: str) -> dict:
        """
        Delete a candidate
        :param personal_id_: personal id of the candidate
        :return:
        """
        print("Delete candidate" + personal_id_)
        return self.candidate_repository.delete(personal_id_)

    def party_assign(self, candidate_id: str, party_id: str) -> dict:
        """

        :param candidate_id:
        :param party_id:
        :return:
        """
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        party_dict = self.party_repository.find_by_id(party_id)
        party_obj = Party(party_dict)
        candidate_obj.party = party_obj
        return self.candidate_repository.save(candidate_obj)
