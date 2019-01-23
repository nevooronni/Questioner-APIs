from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.utils import generate_id
from .base_model import Model

users = []

class User(Model):
  """
    Model class for user object
  """

  def __init__(self):
    super().__init__(users)

  def save(self, data):
    """
      method to save new user
    """

    data['id'] = generate_id(users)
    data['password'] = generate_password_hash(data['password'])
    data['registered_on'] = datetime.now()
    data['modified_on'] = datetime.now()
    data['is_admin'] = False

    users.append(data)
    return data

  @staticmethod
  def check_password(self, hash, password):
    """
      method to check if the passwords match
    """

    return check_password_hash(hash, password)

