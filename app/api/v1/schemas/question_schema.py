from marshmallow import Schema, fields, post_dump
from ..utils.validator import required

class QuestionSchema(Schema):
  """
    class for validating question object schema
  """

  id = fields.Int(dump_only=True)
  title = fields.Str(required=True, validate=(required))
  body = fields.Str(required=True, validate=(required))
  meetup = fields.Int(required=True)
  created_by = fields.Int(required=True)
  votes = fields.Int(dump_only=True)
  created_on = fields.DateTime(dump_only=True)
  modified_on = fields.DateTime(dump_only=True)