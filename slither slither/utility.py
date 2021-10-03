from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By


class Utility:
    def __init__(self, driver) -> None:
        self.driver = driver

 

    def clickOnElement(self, xpath, waitTime):
            
            element = WebDriverWait(self.driver, waitTime).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()

    def clickOnElementJs(self, xpath, waitTime):
            element = WebDriverWait(self.driver, waitTime).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))

            javascript = """
            function getElementByXpath(path) {
                return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            }
            """
            part2 = " getElementByXpath(\"%s\").click()" %(xpath)
            javascript = javascript + part2
            self.driver.execute_script(javascript)

           
           
           
           
           
           
