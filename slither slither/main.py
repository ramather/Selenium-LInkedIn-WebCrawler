from page import Page
from search import Search
from selenium import webdriver
from utility import Utility
import unittest
from login import LoginPage
from page import Page


class LinkedInSearch(unittest.TestCase):
    def setUp(self):
        # add path to your webdriver here and make sure it is the same as your current chrome
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.linkedin.com/")
        self.driver.maximize_window()
        self.utility = Utility(self.driver)
    
    def test_search_for_jobs(self):
        loginObj = LoginPage(self.driver, self.utility)
        searchObj = Search(self.driver, self.utility)
        # enter your username and password here
        loginObj.logIn("", "")
        searchObj.searchForJobs("Software Developer")
        searchObj.clickOnJobs()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

