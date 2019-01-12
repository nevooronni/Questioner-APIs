from flask import jsonify, request, abort, make_response
from ...v1 import version_1 as v1
from ..schemas.question_schema import QuestionSchema 
from ..models.question_model import Question
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db = Question()

@v1.route('/questions', methods=['POST'])
def create_question():
  """
    Endpoint for creating a question
  """

  req_data = request.get_json()

  if not req_data:
    abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

  data, errors = QuestionSchema().load(req_data)
  if errors:
    abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': 'errors'}), 400))
  
  question = db.save(data)
  response = QuestionSchema().dump(question).data
  return jsonify({'status': 201, 'message': 'question created succesfully', 'data': response}), 201