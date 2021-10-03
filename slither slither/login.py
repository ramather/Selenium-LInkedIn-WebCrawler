from utility import Utility
from locators import Locators
from page import Page


class LoginPage(Page):
    # def __init__(self, driver, utility) -> None:
    #     self.driver = driver
    #     self.utility = utility

    def logIn(self, username, password):
        self.utility.clickOnElement(Locators.usernameField_xpath, 5)
        self.driver.find_element_by_xpath(Locators.usernameField_xpath).send_keys(username)
        self.driver.find_element_by_xpath(Locators.passwordField_xpath).send_keys(password)
        self.utility.clickOnElement(Locators.signIn_xpath, 5)



