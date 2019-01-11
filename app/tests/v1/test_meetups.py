from flask import json
from .base_test import BaseTest
from app.api.v1.models.meetup_model import meetups

class TestMeetups(BaseTest):
  """
    Test class for meetup
  """

  def setUp(self):
    """
      setup method for initializing varialbes
    """

    self.headers = {'Content-Type': 'application/json'}
    super().setUp()

    self.meetup = {
      'topic': 'Marvel Avengers Meetup',
      'location': 'Time Towers, Nairobi',
      'happening_on': '14/01/2019',
      'tags': ['comics', 'marvel universe']
    }

    self.meetup2 = {
      'topic' : 'Nairobi Data Science Meetup',
      'location' : 'Jakaranda Hotel, Nairobi',
      'happening_on' : '08/01/2019',
      'tags' : ['python', 'R program', 'data science']
    }

    self.meetup_with_no_location = {
      'topic': 'Marvel Avengers Meetup',
      'happening_on': '14/01/2019',
      'tags': ['python', 'flask']
    }

    self.meetup_with_empty_location = {
      'topic': 'Marvel Avengers Meetup',
      'location': '',
      'happening_on': '14/01/2019',
      'tags': ['python', 'flask']  
    }

  def tearDown(self):
    """
      teardown method empty all initialized variables
    """

    meetups.clear()
    super().tearDown()

  def test_create_meetup_with_no_data(self):
    """
      Test create meetup with no data provided
    """
    res = self.client.post('/api/v1/meetups')
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'No data provided')

  def test_create_meetup_empty_data(self):
    """
      Test create meetup method with emtpy data
    """
    meetup = {}

    res = self.client.post('/api/v1/meetups', json=json.dumps(meetup), headers=self.headers)  
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_create_meetup_with_missing_fields(self):
    """
      Test create meetup method with missing fields
    """

    res = self.client.post('/api/v1/meetups', json=self.meetup_with_no_location, headers=self.headers)
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_create_meetup_with_empty_fields(self):
    """
      Test create meetup method with empty fields
    """

    res = self.client.post('/api/v1/meetups', json=self.meetup_with_empty_location, headers=self.headers)
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_create_meetup(self):
    """
      Test create meetup method
    """
    res = self.client.post('/api/v1/meetups', json=self.meetup, headers=self.headers)
    data = res.get_json()

    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['status'], 201)
    self.assertEqual(data['message'], 'meetup created succesfully')

  def test_fetch_specific_meetup(self):
    """
      Test method for fetching a specific meetup
    """

    self.client.post('/api/v1/meetups', json=self.meetup, headers=self.headers)
    self.client.post('/api/v1/meetups', json=self.meetup_2, headers=self.headers)

    res = self.client.get('/api/v1/meetups/1')
    data = res.get_json()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['status'], 200)
    self.assertEqual(data['data']['id'], 1)

  def test_fetch_non_existent_meetup(self):
    """
      Test method for fetching a meetup that doesn't exist
    """
    res = self.client.get('/api/v1/meetups/14')
    data = res.get_json()

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['status'], 404)
    self.assertEqual(data['message'], 'meetup not found')
  