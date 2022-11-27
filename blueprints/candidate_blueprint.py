from flask import Blueprint
from flask import request

from controllers.candidate_controller import CandidateController


candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()


@candidate_blueprints.route("/candidate/all", methods=['GET'])
def get_all_candidate():
    """
    Controller brings all candidate in the database
    :return: all candidate in the database and 200 code successful get
    """
    response = candidate_controller.index()
    return response, 200


@candidate_blueprints.route("/candidate/<string:personal_id>", methods=['GET'])
def get_candidate_by_personal_id(personal_id):
    """
    Controller brings a specific candidate in the database
    :param personal_id: candidate personal id
    :return: a candidate and 200 successful code get
    """
    response = candidate_controller.show(personal_id)
    return response, 200


@candidate_blueprints.route("/candidate/insert", methods=['POST'])
def insert_candidate():
    """
    The information on the body is parsed from json to dictionary and
    the controller create a new candidate
    :return: a dictionary with the information of the new candidate and a success post code 201
    """
    candidate = request.get_json()
    response = candidate_controller.create(candidate)
    return response, 201


@candidate_blueprints.route("/candidate/update/<string:personal_id>", methods=['PATCH'])
def update_candidate(personal_id):
    """
    The information on the body is parsed from json to dictionary and the controller is called
    and load with the dictionary and the personal_id in the url
    :param personal_id:
    :return: a dictionary with a success message update and a success post code 201
    """
    candidate = request.get_json()
    response = candidate_controller.update(personal_id, candidate)
    return response, 201


@candidate_blueprints.route("/candidate/<string:candidate_id>/party/<string:party_id>", methods=['PUT'])
def assign_party(candidate_id: str, party_id: str):
    """
    The controller joint a candidate and a party
    :param candidate_id: Candidate id
    :param party_id: Party id
    :return: a dictionary with the information of both entities and a success post code 201
    """
    response = candidate_controller.party_assign(candidate_id, party_id)
    return response, 201


@candidate_blueprints.route("/candidate/delete/<string:personal_id>", methods=['DELETE'])
def delete_candidate(personal_id):
    """
    Controller delete a specific candidate in the database with the personal_id in the url
    :param personal_id: candidate personal id
    :return: a dictionary with a success message delete and a success eliminate code 204 Not content
    """
    response = candidate_controller.delete(personal_id)
    return response, 204
