import json

from flask import Flask
from mysql_db.declaration import DataBaseDeclaration
app = Flask(__name__)
from flask_cors import CORS, cross_origin
db = DataBaseDeclaration()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def create_json_response(status=200, data=[]):
        data_to_show = json.dumps({"content" :data[:10], "totalSize": 10}, indent=4)
        response = app.response_class(response=data_to_show, status=status, mimetype='application/json')
        return response

@app.route('/getData')
@cross_origin()
def hello_world():
    return create_json_response(data=db.retrieve("TWEET"))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
