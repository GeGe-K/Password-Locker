class User:
  """
  Class that generates details about the user

  """

  user_list = [] #Empty password list

  def __init__(self,username,password):
    '''
    __init__ method for definition of object properties.

    Args:
        username:Username of the new user.
        password:Password of the new user.

    '''
  
    self.username = username 
    self.password = password

  def save_user(self):
    '''
    save_user method saves user objects into user_list
    '''

    User.user_list.append(self)

  def delete_user(self):
    '''
    delete_user method deletes a saved user from user_list
    '''
    User.user_list.remove(self)

  @classmethod
  def user_exists(cls,username):
        '''
        Method that checks if a user exists in the user_list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending on if the user exists or not
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False    

  @classmethod
  def display_users(cls):
    '''
    method which returns user list
    '''

    return cls.user_list

class Credentials:
  '''
  class that generates new instances of the user's credentials
  '''

  credentials_list=[] #empty credentials list

  def __init__(self,account_name,username,password):
    '''
    __init__ method for definition of object properties.

    Args:
        account_name:New credentials account name.
        username:New credentials username.
        password:New credentials password .

    '''
    self.account_name = account_name
    self.username = username 
    self.password = password