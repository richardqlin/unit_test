# assertIN & assertNotIn

import unittest

class Test(unittest.TestCase):
    def testName(self):
        lst = {'python','selenium', 'java'}
        #self.assertIn('python',lst)
        #self.assertIn('c++',lst)

        #self.assertNotIn('python',lst)
        self.assertNotIn('c++', lst)


if __name__ == '__main__':
    unittest.main()