from models.vote import Vote
from repositories.vote_repository import VoteRepository


class VoteController:

    def __init__(self):
        print("Vote controller ready...")
        self.vote_repository = VoteRepository()

    def create(self, vote_: dict) -> dict:
        """
        Inset a new vote
        :param vote_: dictionary with candidate personal id and table number
        :return:
        """
        print("Get all vote")
        vote = Vote(vote_)
        return self.vote_repository.save(vote)



