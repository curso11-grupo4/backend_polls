from repositories.reports_repository import ReportRepository


class ReportsControllers:
    def __init__(self):
        self.reports_repository = ReportRepository()

    def get_highest_vote(self):
        return self.reports_repository.get_highest_vote()