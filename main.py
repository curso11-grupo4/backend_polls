import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidate_blueprint import candidate_blueprints
from blueprints.party_blueprint import party_blueprints
from blueprints.table_blueprint import table_blueprints
from blueprints.vote_blueprint import vote_blueprints
from blueprints.reports_blueprint import reports_blueprints


app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(party_blueprints)
app.register_blueprint(vote_blueprints)
app.register_blueprint(table_blueprints)
app.register_blueprint(reports_blueprints)


@app.route("/", methods=['GET'])
def home():
    """
    Root endpoint
    :return: a response dictionary is converted to json
    """
    response = {"message": "Welcome"}
    return jsonify(response)


def load_file_config():
    """
    Convert the connection data from json to a dictionary
    :return: Python dictionary
    """
    with open("config.json", 'r') as config_file:
        data = json.load(config_file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
