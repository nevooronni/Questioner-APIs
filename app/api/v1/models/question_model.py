from datetime import datetime
from .base_model import Model
from ..utils.utils import generate_id

questions = []

class Question(Model):
    """
      Class for meetup object
    """
    def __init__(self):
      super().__init__(questions)

    def save(self, data):
      """ 
        method to add a new question
      """
      data['id'] = generate_id(self.collection)
      data['votes'] = 0
      return super().save(data)

    