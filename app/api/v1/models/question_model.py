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

    def check_if_it_exists(self, key, value):
      """
        method to check if a question exists
      """

      questions_returned = [question for question in questions if value == question[key]]
      return len(questions_returned) > 0 

    def upvote_question(self, question_id):
      """
        method to upvote a quesiton
      """

      for question in questions:
        if question['id'] == question_id:
          question['votes'] = question['votes']+1

        return question

    def downvote_question(self, question_id):
      """
        method to downvote a question
      """

      for question in questions:
        if question['id'] == question_id:
          question['votes'] = question['votes']-1
        
        return question

    