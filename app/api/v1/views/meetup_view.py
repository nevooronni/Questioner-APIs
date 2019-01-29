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

@v1.route('/meetups/<int:meetup_id>', methods=['GET'])
def fetch_meetup(meetup_id):
  """ 
    Endpoint for fetching a specific meetup
  """

  if not db.check_if_it_exists('id', meetup_id):
    abort(make_response(jsonify({'status': 404, 'message': 'meetup not found'}), 404))
  
  meetup = db.find('id', meetup_id)
  data = []
  data.append(MeetupSchema().dump(meetup).data)
  return jsonify({'status': 200, 'data': data}), 200

@v1.route('/meetups/upcoming', methods=['GET'])
def fetch_all_upcoming_meetups():
  """
    Endpoing for fetching all upcoming meetups
  """

  meetups = db.fetch_all()
  response = MeetupSchema(many=True).dump(meetups).data
  return jsonify({'status': 200, 'data': response}), 200

@v1.route('/meetups/<int:meetup_id>/<string:rsvps>', methods=['POST'])
def rsvps_meetup(meetup_id, rsvps):
  """
    Enpoint for rsvps a meetup
  """

  valid_reponses = ('yes', 'maybe', 'no')

  if not db.check_if_it_exists('id', meetup_id):
    return jsonify({'status': 404, 'message': 'Error meetup not found!'}), 404

  if rsvps not in valid_reponses:
    return jsonify({'status': 400, 'message': 'Error invalid rsvp!'}), 400

  meetup = db.fetch_meetup_by_id(meetup_id)
  return jsonify({
    'status': 200,
    'message': 'rsvp created successfully',
    'data': [{
      'meetup': meetup['id'],
      'topic': meetup['topic'],
      'status': rsvps
    }]
  }), 200




  