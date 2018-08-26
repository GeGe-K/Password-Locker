#!/usr/bin/env python3.6
from user import User,Credentials

def create_user(username,password):
    '''
    function to create new user
    '''
    new_user = User(username,password)
    return new_user
def save_users(user):
  '''
  to save user
  '''
  user.save_user()

def del_user(user):
  '''
  deletes a contact
  '''
  user.delete_user()

def check_existing_users(username):
  '''
  checks if a contact exists with the username and returns a boolean
  '''
  return User.user_exists(username)

def display_users():
  '''
  returns all saved contacts
  '''
  return User.display_users()

if __name__ == '__main__':

    main()