from marshmallow import Schema, fields, post_dump
from ..utils.validator import required
from ..models.user_model import User

class MeetupSchema(Schema):
  """
    class to validate meetup object schema
  """

  id = fields.Int(dump_only=True)
  topic = fields.Str(required=True, validate=(required))
  location = fields.Str(required=True, validate=(required))
  happening_on = fields.Str(required=True, validate=(required))
  tags = fields.List(fields.Str(), required=False)
  images = fields.List(fields.Str(), required=False)