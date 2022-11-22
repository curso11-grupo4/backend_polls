from models.vote import Vote
from repositories.interfaceRepository import  InterfaceRepository



class ReportRepository(InterfaceRepository[Vote]):
    def get_highest_vote(self):
        query_aggregation = {

        }
        pipline =[query_aggregation]
        return self.query_aggregation(pipline)