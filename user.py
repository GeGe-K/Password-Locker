class User:
  """
  Class that generates details about the user

  """

  password_list = [] #Empty password list

def __init__(self,username,password):
  '''
  __init__ method for definition of object properties.

  Args:
      username:Username of the new user.
      password:Password of the new user.

  '''
  self.username = username 
  self.password = password