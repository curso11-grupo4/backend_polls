from repositories.reports_repository import ReportsRepository


class ReportsController:
    def __init__(self):
        """
        Constructor of the ReportsController class
        """
        self.reports_repository = ReportsRepository()

    def get_votes_table(self):
        return self.reports_repository.get_votes_by_table()

    def get_votes_candidate(self):
        return self.reports_repository.get_votes_by_candidate()

    def get_votes_party(self):
        return self.reports_repository.get_votes_by_party()

    def get_distribution(self):
        return self.reports_repository.distribution_by_parties()

