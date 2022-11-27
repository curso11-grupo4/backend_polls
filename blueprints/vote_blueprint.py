from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/votes/all", methods=['GET'])
def get_all_vote():
    response = vote_controller.index()
    return response, 200


@vote_blueprints.route("/vote/<string:vote_id_>", methods=['GET'])
def get_vote_by_id(vote_id_):
    response = vote_controller.show(vote_id_)
    return response, 200


@vote_blueprints.route("/vote/insert/candidate/<string:candidate_id>/table/<string:table_id>", methods=['POST'])
def insert_vote(candidate_id, table_id):
    """
    The information on the body is parsed from json to dictionary and
    the controller create a new vote
    :param candidate_id: candidate id
    :param table_id: table id
    :return: a dictionary with the information of the new vote and a success post code 201
    """
    vote = request.get_json()
    response = vote_controller.create(vote, candidate_id, table_id)
    return response, 201
