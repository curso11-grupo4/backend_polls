
class CandidateController:

    def __init__(self):
        print("Candidate controller ready...")

    def index(self) ->list:
        """
        Get all candidate with number of resolution, personal_id, name and lastname
        :return:
        """
        print("Get all tables")

    def show(self, personal_id_: str) -> dict:
        """
        Get a specific candidate with the personal id
        :param personal_id_:
        :return:
        """
        print("Get a candidate")

    def create(self, candidate_: dict) -> dict:
        """
        Insert a new candidate
        :param candidate_: a dictionary carries personal id, resolution number, name and lastname
        :return:
        """
        print("Insert a new candidate")

    def update(self, personal_id_: str, candidate_: dict) ->dict:
        """
        Update a specific candidate
        :param personal_id_: candidate's personal_id
        :param candidate_: a dictionary with resolution number, name and lastname
        :return:
        """
        print("Update a candidate")

    def delete(self, personal_id_: str) -> dict:
        """
        Delete a candidate
        :param personal_id_: personal id of the candidate
        :return:
        """
        print("Delete candidate")

