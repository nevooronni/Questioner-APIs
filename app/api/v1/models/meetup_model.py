from datetime import datetime
from ..utils.utils import generate_id
from .base_model import Model

meetups = []

class Meetup(Model):
  """
    Class for meetup object
  """

  def __init__(self):
    super().__init__(meetups)

  def save(self, data):
    """
      method to add a new meetup
    """

    data['id'] = generate_id(self.collection)
    return super().save(data)