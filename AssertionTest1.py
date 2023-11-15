import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='C:/Users/richardlin/Downloads/chromedriver_win32_2/chromedriver.exe')
        driver.get('https://www.google.com')
        titleOfWebPage  = driver.title
        #assertEqual
        self.assertEqual('Google', titleOfWebPage, 'webpage title is not same')
        #self.assertNotEqual('Google123',titleOfWebPage)




if __name__=='__main__':
    unittest.main()