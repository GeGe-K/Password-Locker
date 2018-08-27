#!/usr/bin/env python3.6
import string
import random
from random import choice
from user import User,Credential

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User (username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def find_user(username):
    '''
    Funtion that finds a user by a login and returns the user
    '''
    return  User.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return  User .user_exists(username)

def create_credential(account_name,username,password):
    '''
    Function that creates a new credential
    '''
    new_credential = Credential (account_name,username,password)
    return new_credential

def save_credential(credential):
    '''
    saves a credential
    '''
    credential.save_credential()


def delete_credential(account_name):
    '''
    deletes a credential
    '''
    Credential.delete_credential(account_name)

def find_credential(account_name):
    '''
    finds a credential by account_name and returns the credential
    '''
    return Credential.find_by_account_name(account_name)

def check_existing_credentials(account_name):
    '''
    checks if a credential exists with that account_name and returns a Boolean value
    '''
    return Credential.credential_exist(account_name)

def display_credential():
    '''
    returns all saved credentials
    '''
    return Credential.display_credential()



def main():
    print("Hello Welcome to your user list.What is your name?")
    user_name = input()
    print(f"Hello {user_name}.what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: cu - create a new user ,du - display users,fa - find account,fu- find a user,cc- create a new credential, gp - generate new password ,da- delete account ,ex - exit user list")
        in_short_code = input().lower()


        if in_short_code == 'cu':
            print("Create a new user account by following the following steps:")
            print("Enter any username you wish to use for your account")
            username = input()
            print("Enter password:")
            password = input()

            save_users(create_user(username,password))
            print('\n')
            print(f"Thank you {username}, you may now proceed to open up your account")
            print('\n')

        elif in_short_code == 'fu':
            print(" \n Enter any username to find user: \n")
            search_username = input()
            if check_existing_users(search_username):
                search_user = find_user(search_username)
                print(f"{search_user.username}")
                print(f"Password.......{search_user.password}")
            else:
                 print("Sorry,This account does not exist!")

        elif in_short_code =='ex' :
            print("Try again later,Goodbye!...")
            break
            
                    

        elif in_short_code == 'cc':
                        print('\n')
                        print("Follow the following steps to create a new credential;")
                        print('\n')
                        print("Enter the account name i.e Instagram/Facebook/Twitter")
                        account_name=input()
                        print("Enter your username for the new account:")
                        username=input()
                        print("Enter password:")
                        password=input()
                        save_credential(create_credential(account_name,username,password))
                        print('\n')
                        print(f"You have successfully created a new credential for your new {account_name} account.")
                        print('\n')

        elif in_short_code == 'gp':
                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(choice(alphabet) for i in range(8))
                        print(f"Your new generated password is: {password} \n")
                      

        elif in_short_code == 'dc':
                        print('/n')
                        if display_credential():
                            print("Below is a list of all your credentials:")
                            print('\n')
                            for credential in display_credential():
                                print(f"Account: {credential.account_name}")
                                print(f"Username: {credential.username}")
                                print(f"Password: {credential.password}")
                                print('\n')
                        else:
                            print("\n Sorry,You do not have any credentials to display")


                



        else:
                print("That account does not exist")

    else:
            print("Short code not found,Please use the short codes")

        
                
if __name__ == '__main__':
    main()



