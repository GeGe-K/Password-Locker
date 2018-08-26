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

def main():
  print("Hello Welcome to your user list.What is your name?")
  user_name = input()
  print(f"Hello {user_name}.what would you like to do?")
  print('\n')

  while True:
    print("Use these short codes: cu - create new user,du - display users,fu- find a user,ex - exit user list")

    short_code = input().lower()

    if short_code == 'cu':
      print("New User")
      print("-"*10)

      print("Username ...")
      username=input()

      print("Password ...")
      password=input()

      save_users (create_user (username,password)) #create and save new user
      print('\n')
      print(f"New User {username} {password} created")
      print('\n')

    elif short_code == 'du':
      if display_users():
        print("Here is a list of all your users")
        print('\n')

        for user in display_users():
          print(f"{user.username}..... {user.password}")
        print('\n')
      else:
        print('\n')
        print("You don't have any users saved yet")
        print('\n')

    elif short_code == "ex":
      print("Bye....")
      break
    else:
      print("I really didn't get that.Please use the short codes")
  

if __name__ == '__main__':

    main()