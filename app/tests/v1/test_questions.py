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
    self.headers = {'Content-Type': 'application/json'}
    self.question = {}
    self.question_with_missing_fields = {
      'title': 'Javascript Intro'
    }
    self.question_with_valid_data = {
      'title': 'Javascript Intro',
      'body' : 'Vanilla js or ES6',
      'meetup' : 5,
      'created_by' : 2
    }
    super().setUp()

  def tearDown(self):
    """
      teardown method empty all initialized variables
    """
    questions.clear()
    super().tearDown()
  
  def test_create_question_with_no_data(self):
    """
      Test method for creating a question with no data
    """

    res = self.client.post('/api/v1/questions')
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'No data provided')

  def test_create_question_with_empty_data(self):
    """
      Test method for creating a question with empty data
    """

    res = self.client.post('/api/v1/questions', json=json.dumps(self.question), headers=self.headers)
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_create_question_with_missing_fields(self):
    """
      Test method for creating a question with missing fields
    """

    res = self.client.post('/api/v1/questions', json=self.question_with_missing_fields, headers=self.headers)
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_create_question_with_valid_data(self):
    """
      Test method for creating question with valid data
    """

    res = self.client.post('/api/v1/questions', json=self.question_with_valid_data, headers=self.headers)
    data = res.get_json()

    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['status'], 201)
    self.assertEqual(data['message'], 'question created succesfully')
  
  def test_upvote_on_question_not_posted(self):
    """
      Test upvote/downvote method on a question that doesn't exist
    """
    res = self.client.patch('/api/v1/questions/15/upvote')
    data = res.get_json()

    self.assertEqual(res.status_code, 404)stion created succesfully')
    self.assertEqual(data['status'], 404)
    self.assertEqual(data['message'], 'question not found')
