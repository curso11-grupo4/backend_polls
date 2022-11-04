from flask import Blueprint
from flask import request

from controllers.party_controller import PartyController


party_blueprints = Blueprint('party_blueprints', __name__)
party_controller = PartyController()


@party_blueprints.route("/party/all", methods=['GET'])
def get_all_parties():
    response = party_controller.index()
    return response, 200


@party_blueprints.route("/party/<string:_id>", methods=['GET'])
def get_party_by_id(_id):
    response = party_controller.show(_id)
    return response, 200


@party_blueprints.route("/party/insert", methods=['POST'])
def insert_party():
    party = request.get_json()
    response = party_controller.create(party)
    return response, 201


@party_blueprints.route("/party/update/<string:_id>", methods=['PATCH'])
def update_party(_id):
    party = request.get_json()
    response = party_controller.update(_id, party)
    return response, 201


@party_blueprints.route("/party/delete/<string:_id>", methods=['DELETE'])
def delete_party(_id):
    response = party_controller.delete(_id)
    return response, 204
