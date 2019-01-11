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
      'tags': ['python', 'flask']
    }

  def tearDown(self):
    """
      teardown method empty all initialized variables
    """

    meetups.clear()
    super().tearDown()