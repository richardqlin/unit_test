# assertTrue or assertFalse

import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='C:/Users/richardlin/Downloads/chromedriver_win32_2/chromedriver.exe')
        driver.get('https://www.google.com')

        titleOfWebPage = driver.title

        #self.assertTrue(titleOfWebPage == 'Google')

        self.assertFalse(titleOfWebPage =='Google123')


if __name__=='__main__':
    unittest.main()
