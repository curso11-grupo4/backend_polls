from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/vote/insert/candidate/<string:candidate_id>/table/<string:table_id>", methods=['POST'])
def insert_vote(candidate_id, table_id):
    vote = request.get_json()
    response = vote_controller.create(vote, candidate_id, table_id)
    return response, 201
