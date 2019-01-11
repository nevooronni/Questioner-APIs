from flask import jsonify, request, abort, make_response
from ...v1 import version_1 as v1
from ..schemas.meetup_schema import MeetupSchema
from ..models.meetup_model import Meetup
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db = Meetup()

@v1.route('/meetups', methods=['POST'])
def create_meetup():
  """
    Endpoint for creating a meetup
  """
  req_data = request.get_json()

  if not req_data:
    abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

  data, errors = MeetupSchema().load(req_data)
  if errors:
    abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': errors}), 400))

  new_meetup = db.save(data)
  response = MeetupSchema().dump(new_meetup).data
  return jsonify({
    'status': 201, 
    'message': 
    'meetup created succesfully', 
    'data':[response]
  }), 201


  