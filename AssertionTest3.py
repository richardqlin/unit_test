#assertIsNone & assertIsNotNone

import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='C:/Users/richardlin/Downloads/chromedriver_win32_2/chromedriver.exe')
        #driver.get('https://www.google.com')
        #driver = None
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)



if __name__ == '__main__':
    unittest.main()