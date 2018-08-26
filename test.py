import unittest
import pyperclip
from user import User,Credentials

class TestUser(unittest.TestCase):

      '''
      Test class that defines test cases for the user class

      Args:
          unittest.TestCase: TestCase class helping to create test cases
      '''

      def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gift-Lumumba","gL0711419032") #creates user object

      def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Gift-Lumumba")
        self.assertEqual(self.new_user.password,"gL0711419032")

      def test_save_user(self):
        '''
        test_save_user test case to test if the user object has been saved into the user list
        '''
        self.new_user.save_user()#saving new user
        self.assertEqual(len(User.user_list),1)

      def tearDown(self):
        '''
        tearDown method which does clean up after each test has run.
        '''
        User.user_list = [] 

      def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","gL1999")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

      def test_delete_user(self):
        '''
        test_delete_user to test if it's possible to remove a user from user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","gL1999") #added contact
        test_user.save_user()

        self.new_user.delete_user() #deletes user object
        self.assertEqual(len(User.user_list),1)

      def test_user_exists(self):
        '''
        test to check whether a user exists or not.
        '''
        self.new_user.save_user()
        test_user = User("Test","gL1998") # new user created
        test_user.save_user()

        user_exists =User.user_exists("Test")

        self.assertTrue(user_exists)
      
      def test_display_all_users(self):
        '''
        method that returns a list of all users saved in the user_list
        '''

        self.assertEqual( User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
      '''
      Test class that defines test cases for credentials class behaviours.

      Args:
      unittest.TestCase:TestCase class helping in creating test cases
      '''   

      def setUp(self):
        '''
        Set up method to run before each test cases.
        ''' 
        self.new_credentials = Credentials ("Facebook","Gift Lumumba","0721851691") #created credentials object

      def tearDown(self):
        '''
        tearDown method that does clean up after each test has been run
        '''  
        Credentials.credentials_list = []

      def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name,"Facebook")
        self.assertEqual(self.new_credentials.username,"Gift Lumumba")
        self.assertEqual(self.new_credentials.password,"0721851691")

      def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object has been saved into the credentials list
        '''  
        self.new_credentials.save_credentials() #saving new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

      def test_save_multiple_credentials(self):
        '''
        method that checks if we can save multiple credentials objects to credentials_list
        '''  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","Gift-Lumumba","gL0711419032")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

      def test_delete_credentials(self):
        '''
        tests if we can delete a credential from our credentials list
        '''  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","Gift-Lumumba","gL0711419032")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #deletes credentials object
        self.assertEqual (len(Credentials.credentials_list),1)

      def test_find_credentials_by_account_name(self):
        '''
        to check if we can find a credential by the account name and display more information about it
        '''  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","Gift-Lumumba","gL0711419032")
        test_credentials.save_credentials()

        found_credentials =Credentials.find_by_account_name("Github")
        self.assertEqual(found_credentials.password,test_credentials.password)

      def test_credentials_exists(self):
        '''
        checks if we can return a boolean if we cannot find the credentials
        '''  

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","Gift-Lumumba","gL0711419032")
        test_credentials.save_credentials()

        credentials_exists =Credentials.credentials_exist("Github")
        self.assertTrue(credentials_exists)

      def test_display_all_credentials(self):
        '''
        returns a list of all credentials saved 
        '''  

        self.assertEqual( Credentials.display_credentials(),Credentials.credentials_list)

      def test_copy_account_name(self):
        '''
        test to confirm we are copying the account name from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials .copy_account_name("Facebook")

        self.assertEqual(self.new_credentials.account_name,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
