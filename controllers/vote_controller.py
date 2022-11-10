from models.vote import Vote
from models.candidate import Candidate
from models.table import Table
from repositories.vote_repository import VoteRepository
from repositories.candidate_repository import CandidateRepository
from repositories.table_repository import TableRepository


class VoteController:

    def __init__(self):
        print("Vote controller ready...")
        self.vote_repository = VoteRepository()
        self.candidate_repository = CandidateRepository()
        self.table_repository = TableRepository()

    def create(self, vote_: dict, candidate_id: str, table_id: str) -> dict:
        """
        Inset a new vote
        :param table_id:
        :param candidate_id:
        :param vote_: dictionary with candidate personal id and table number
        :return:
        """
        vote = Vote(vote_)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        vote.candidate = candidate_obj
        vote.table = table_obj
        return self.vote_repository.save(vote)



