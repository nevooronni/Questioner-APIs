"""configurations for the app"""

import os

class Config(object):
  """
    Parent configuration class.
  """

  DEBUG = True
  SECRET_KEY = os.getenv('SECRET_KEY')