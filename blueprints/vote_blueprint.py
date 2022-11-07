from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/vote/insert", methods=['POST'])
def insert_vote():
    vote = request.get_json()
    response = vote_controller.create(vote)
    return response, 201
