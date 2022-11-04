from flask import Blueprint
from flask import request

from controllers.table_controller import TableController


table_blueprints = Blueprint('table_blueprints', __name__)
table_controller = TableController()


@table_blueprints.route("/table/all", methods=['GET'])
def get_all_tables():
    response = table_controller.index()
    return response, 200


@table_blueprints.route("/table/<string:table_number>", methods=['GET'])
def get_table_by_number(table_number):
    response = table_controller.show(table_number)
    return response, 200


@table_blueprints.route("/table/insert", methods=['POST'])
def insert_table():
    """
    The data come in the body as a json. It is converted to dictionary and the data es save in table
    :return:
    """
    table = request.get_json()
    response = table_controller.create(table)
    return response, 201


@table_blueprints.route("/table/update/<string:table_number>", methods=['PATCH'])
def update_table(table_number):
    table = request.get_json()
    response = table_controller.update(table_number, table)
    return response, 201


@table_blueprints.route("/table/delete/<string:table_number>", methods=['DELETE'])
def delete_table(table_number):
    response = table_controller.delete(table_number)
    return response, 204
