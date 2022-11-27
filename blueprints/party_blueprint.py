from flask import Blueprint
from flask import request

from controllers.party_controller import PartyController


party_blueprints = Blueprint('party_blueprints', __name__)
party_controller = PartyController()


@party_blueprints.route("/party/all", methods=['GET'])
def get_all_parties():
    """
    Controller brings all parties from the database
    :return: all parties in the database and 200 success code
    """
    response = party_controller.index()
    return response, 200


@party_blueprints.route("/party/<string:_id>", methods=['GET'])
def get_party_by_id(_id):
    """
    Controller brings a specific party from the database
    :param _id: party id
    :return: a party and 200 success code
    """
    response = party_controller.show(_id)
    return response, 200


@party_blueprints.route("/party/insert", methods=['POST'])
def insert_party():
    """
    The information on the body is parsed from json to dictionary and
    the controller create a new party
    :return: a dictionary with the information of the new party and a success post code 201
    """
    party = request.get_json()
    response = party_controller.create(party)
    return response, 201


@party_blueprints.route("/party/update/<string:_id>", methods=['PATCH'])
def update_party(_id):
    """
    The information on the body is parsed from json to dictionary and the controller is called
    and load with the dictionary and the _id in the url
    :param _id: party id
    :return: a dictionary with a success message update and a success post code 201
    """
    party = request.get_json()
    response = party_controller.update(_id, party)
    return response, 201


@party_blueprints.route("/party/delete/<string:_id>", methods=['DELETE'])
def delete_party(_id):
    """
    Controller delete a specific party in the database with the _id in the url
    :param _id: party id
    :return: a dictionary with a success message delete and a success eliminate code 204 Not content
    """
    response = party_controller.delete(_id)
    return response, 204
