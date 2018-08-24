class User:
  """
  Class that generates details about the user

  """

  user_list = [] #Empty password list
  def save_user(self):

    '''
    save_user method saves user objects into user_list
    '''

    User.user_list.append(self)

  def __init__(self,username,password):
    '''
    __init__ method for definition of object properties.

    Args:
        username:Username of the new user.
        password:Password of the new user.

    '''
  
    self.username = username 
    self.password = password