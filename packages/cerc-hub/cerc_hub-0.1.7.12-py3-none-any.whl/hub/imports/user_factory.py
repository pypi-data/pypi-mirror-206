"""
User performs user-related crud operations
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2022 Concordia CERC group
Project CoderPeter Yefi peteryefi@gmail.com
"""

from hub.persistence import User
from hub.persistence import UserRoles


class UserFactory:
  """
  UserFactory class
  """

  def __init__(self, db_name, app_env, dotenv_path):
    self._user_repo = User(db_name=db_name, app_env=app_env, dotenv_path=dotenv_path)

  def create_user(self, name: str, application_id: int, password: str, role: UserRoles):
    """
    Creates a new user
    :param name: the name of the user
    :param application_id: the application id of the user
    :param password: the password of the user
    :param role: the role of the user
    """
    return self._user_repo.insert(name, password, role, application_id)

  def update_user(self, user_id: int, name: str, password: str, role: UserRoles):
    """
    Creates a new user
    :param user_id: the id of the user
    :param name: the name of the user
    :param email: the email of the user
    :param password: the password of the user
    :param role: the role of the user
    """
    return self._user_repo.update(user_id, name, password, role)

  def delete_user(self, user_id):
    """
    Retrieve a single user
    :param user_id: the id of the user to delete
    """
    return self._user_repo.delete(user_id)
