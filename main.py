import json

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from waitress import serve


app = Flask(__name__)
cors = CORS(app)


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
