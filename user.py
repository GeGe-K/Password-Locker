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

  def save_credentials(self):

    '''
    save_credentials method that saves credentials object into credentials_list
    '''
    Credentials.credentials_list.append(self)
  def delete_credentials(self):
    '''
    deletes a saved credential from credentials_list
    '''

    Credentials.credentials_list.remove(self)

  @classmethod
  def find_by_account_name(cls,account_name):
    '''
    method that takes in the account name and returns a credential that matches that account name

    Args:
        account_name:Account name to search for 
    Returns:
        Credentials of person that matches the account name
    '''  

    for credentials in cls.credentials_list:
      if credentials.account_name == account_name:
        return credentials

  @classmethod
  def credentials_exist(cls,account_name):
    '''
    checks if a credential exists in the credentials list.
    Args:
        account_name:Account name to search if it exists
    Returns:
        Boolean:True or false depending on if the credential exists    
    '''      
    for credential in cls.credentials_list:
      if credential.account_name == account_name:
        return True

    return False    

  @classmethod
  def display_credentials(cls):
    '''
    returns credentials list
    '''  
    return cls.credentials_list