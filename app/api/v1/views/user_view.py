from flask import jsonify, request
from ...v1 import version_1 as v1
from ..schemas.user_schema import UserSchema
from ..models.user_model import User
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,get_jwt_identity, jwt_refresh_token_required, get_raw_jwt)

db = User()

@v1.route('/', methods=['GET'])
@v1.route('/index', methods=['GET'])
def index():
    return jsonify({'status': 200, 'message': 'Welcome to Questioner'}), 200

@v1.route('/signup', methods=['POST'])
def signup():
    """ Function to register new user """
    res_data = request.get_json()

    if not res_data:
        return jsonify({'status': 400, 'message': 'No data provided'}), 400

    data, errors = UserSchema().load(res_data)
    if errors:
        return jsonify({'status': 400, 'message' : 'Invalid data, please fill all required fields', 'errors': errors}), 400

    if db.user_exists('username', data['username']):
        return jsonify({'status': 409, 'message' : 'Error username already exists'}), 409

    if db.user_exists('email', data['email']):
        return jsonify({'status': 409, 'message' : 'Error email already exists'}), 409

    new_user = db.save(data)
    result = UserSchema(exclude=['password']).dump(new_user).data

    # Generate access 
    access_token = create_access_token(identity=new_user['id'], fresh=True)
    refresh_token = create_refresh_token(identity=new_user['id'])
    return jsonify({
        'status': 201, 
        'message' : 'User created successfully', 
        'data': result, 
        'access_token' : access_token, 
        'refresh_token' : refresh_token
        }), 201
