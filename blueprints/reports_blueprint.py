from flask import blueprints
from controllers.reports_controllers import ReportsController

reports_blueprints = blueprints('reports_blueprints', __name__)
reports_controller = ReportsController()

@reports_blueprints.route("/reports/highest_vote", methods = ['GET'])

def reports_highest_vote():
    response = reports_controller.get_highest_vote()
    return response, 200