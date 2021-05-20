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
from models import db, User,Task
from sqlalchemy import exc

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

#creacion del usuario
@app.route('/user',methods=['POST'])
def create_user():
    email =request.json.get('email', None)
    if not email:
        return jsonify({})
    try:
        user = user.create_user()
        return jsonify(user), 201
    except exc.IntegrityError:
        return jsonify({'error': "Fail in data"}), 404


#creacion del task
@app.route('/task',methods=['POST'])
def create_task():
    text=request.json.get('text',None)
    if not text:
        return jsonify({})
    try:
        task =task.create()
        return jsonify(task), 201
    except exc.IntegrityError:
        return jsonify({'error': "Fail in data"}), 404
     
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


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
def user_by_email_get(email):
    user_by_email=User.get_by_email(email)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        #"user": str(user)
    }
    return jsonify(user_by_email), 200
    
"""
@app.route('/user', methods=['POST'])
def create_user():
    email, password, = request.json.get(
        "email", None
    ), request.json.get(
        "password", None
    )
    if not email or not password:
        return jsonify({'error': "Missing parametre"}), 403
    user = User(email=email, _password=password)
    try:
        user = user.create()
        return jsonify(user), 201
    except exc.IntegrityError:
        return jsonify({'error': "Fail in data"}), 404
"""
@app.route('/user', methods=['DELETE'])
def delete_user():
    user_by_email=User.get_by_email(email)

#all task  -------    3   ------
@app.route('/task', methods=['GET'])
def all_tasks_get(): 
    all_tasks=Task.get_task()
    response_body = {
        "msg": "Hello, this is your response for all task "
    }
    return jsonify(all_tasks), 200

#all task by user  -------    4   ------
@app.route('/task/<user_id>', methods=['GET'])
def task_by_user_get(user_id): 
    task_by_user=Task.get_task_user(user_id)
    
    return jsonify(task_by_user), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
