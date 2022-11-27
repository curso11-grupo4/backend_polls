from flask import Blueprint
from flask import request

from controllers.table_controller import TableController


table_blueprints = Blueprint('table_blueprints', __name__)
table_controller = TableController()


@table_blueprints.route("/table/all", methods=['GET'])
def get_all_tables():
    """
    Controller brings all tables from the database
    :return: all tables in the database and 200 code successful get
    """
    response = table_controller.index()
    return response, 200


@table_blueprints.route("/table/<string:table_number>", methods=['GET'])
def get_table_by_number(table_number):
    """
    Controller brings a specific table from the database
    :param table_number: number of th table
    :return: a dictionary with info of the table and 200 successful code
    """
    response = table_controller.show(table_number)
    return response, 200


@table_blueprints.route("/table/insert", methods=['POST'])
def insert_table():
    """
    The data come in the body as a json.
    It is converted to dictionary and the data is saved in "table"
    :return: a dictionary with the information of the new table
    and a success post code 201
    """
    table = request.get_json()
    response = table_controller.create(table)
    return response, 201


@table_blueprints.route("/table/update/<string:table_number>", methods=['PATCH'])
def update_table(table_number):
    """
    The information on the body is parsed from json to dictionary and the controller is called
    and load with the dictionary and the table_number in the url
    :param table_number: number of the table
    :return: a dictionary with a success message update and a success post code 201
    """
    table = request.get_json()
    response = table_controller.update(table_number, table)
    return response, 201


@table_blueprints.route("/table/delete/<string:table_number>", methods=['DELETE'])
def delete_table(table_number):
    """
    Controller delete a specific table in the database with
    the table_number in the url
    :param table_number:
    :return: a dictionary with a success message delete and a success eliminate code 204 Not content
    """
    response = table_controller.delete(table_number)
    return response, 204
