from flask import json
from .base_test import BaseTest
from app.api.v1.models.question_model import questions

class TestQuestions(BaseTest):
  """
    Test class for Questions
  """
  def setUp(self):
    """ 
      setup method for initializing variables 
    """
    super().setUp()

  def tearDown(self):
    """
      teardown method empty all initialized variables
    """
    questions.clear()
    super().tearDown()
  