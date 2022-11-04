import json

<<<<<<< HEAD
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from waitress import serve

=======
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidate_blueprint import candidate_blueprints
from blueprints.party_blueprint import party_blueprints
from blueprints.table_blueprint import table_blueprints
from blueprints.vote_blueprint import vote_blueprints

>>>>>>> d767541ffcf71fc89fc268763b5ad8773dce1aed

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(party_blueprints)
app.register_blueprint(vote_blueprints)
app.register_blueprint(table_blueprints)



@app.route("/",methods=['GET'])
def test():
    responder = {"message": "Server running ..."}
    return jsonify(responder)


def load_file_config():
    with open("config.json", 'r') as config_file:
        data = json.load(config_file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
