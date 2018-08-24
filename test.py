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


if __name__ == '__main__':
    unittest.main()
