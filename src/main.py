"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#default
@app.route('/user', methods=['GET'])
def user():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(user), 200

#all user -------   1   ------
@app.route('/user', methods=['GET'])
def user_all_get():
    user_all= User.get_all()
    response_body = {
        "msg": "Hello, this is your get all /user response "
    }
    return jsonify(user_all), 200

#all user by email  -------    2   ------
@app.route('/user/<email>', methods=['GET'])
def user_by_email_get(): 
    user_by_email=User.get_user_by_email(email)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        #"user": str(user)
    }
    return jsonify(user_by_email), 200

#all task  -------    3   ------
app.route('/task', methods=['GET'])
def all_tasks_get(): 
    all_tasks=Task.get.all()
    response_body = {
        "msg": "Hello, this is your response for all task "
    }
    return jsonify(all_tasks), 200

#all task by user  -------    4   ------
app.route('/task', methods=['GET'])
def task_by_user_get(): 
    task_by_user=Task.get.id_user()
    response_body = {
        "msg": "Hello, this is your task by user response "
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
