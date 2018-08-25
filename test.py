import unittest
from user import User

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


if __name__ == '__main__':
    unittest.main()
