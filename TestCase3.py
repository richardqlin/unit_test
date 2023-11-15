import unittest

def setUpModule():
    print('setUpModule') # will be executed before executing any class or any method present in the test class

def tearDownModule(): # will be executed after completing everything executing present in the python module
    print('tearDownModule')

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print('This is login test')

    @classmethod
    def tearDown(self): # Execute after all test methods
        print('This is logout test')

    @classmethod
    def setUpClass(cls): # Execute once when the class started
        print('Open application')
        print()
    @classmethod
    def tearDownClass(cls): # Execute once after the class completed
        print('Close application')

    def test_search(self):
        print('This is search test')

    def test_advancedsearch(self):
        print('this is Advanced search test')

    def test_prepaidTecharge(self):
        print('This is prepaid Recharge test')

    def test_postpaidReCharge(self):
        print('This is post paodRecharge test')



if __name__=='__main__':
    unittest.main()