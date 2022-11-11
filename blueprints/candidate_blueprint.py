from flask import Blueprint
from flask import request

from controllers.candidate_controller import CandidateController


candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()


@candidate_blueprints.route("/candidate/all", methods=['GET'])
def get_all_candidate():
    response = candidate_controller.index()
    return response, 200


@candidate_blueprints.route("/candidate/<string:personal_id>", methods=['GET'])
def get_candidate_by_personal_id(personal_id):
    response = candidate_controller.show(personal_id)
    return response, 200


@candidate_blueprints.route("/candidate/insert", methods=['POST'])
def insert_candidate():
    candidate = request.get_json()
    response = candidate_controller.create(candidate)
    return response, 201


@candidate_blueprints.route("/candidate/update/<string:personal_id>", methods=['PATCH'])
def update_candidate(personal_id):
    candidate = request.get_json()
    response = candidate_controller.update(personal_id, candidate)
    return response, 201


@candidate_blueprints.route("/candidate/<string:candidate_id>/party/<string:party_id>", methods=['PUT'])
def assign_party(candidate_id: str, party_id: str):
    response = candidate_controller.party_assign(candidate_id, party_id)
    return response, 201


@candidate_blueprints.route("/candidate/delete/<string:personal_id>", methods=['DELETE'])
def delete_candidate(personal_id):
    response = candidate_controller.delete(personal_id)
    return response, 204
