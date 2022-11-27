from flask import Blueprint

from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/votes_table", methods=['GET'])
def reports_vote_by_table():
    response = reports_controller.get_votes_table()
    return response, 200


@reports_blueprints.route("/reports/votes_candidate", methods=['GET'])
def reports_vote_by_candidate():
    response = reports_controller.get_votes_candidate()
    return response, 200


@reports_blueprints.route("/reports/votes_party", methods=['GET'])
def reports_vote_by_party():
    response = reports_controller.get_votes_party()
    return response, 200


@reports_blueprints.route("/reports/distribution", methods=['GET'])
def congress_distribution():
    response = reports_controller.get_distribution()
    return response, 200
