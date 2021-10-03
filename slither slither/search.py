from job import Job
from locators import Locators
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from page import Page



class Search(Page):
    indexes_list = []

    # the sleep time might need to be changed based on your internet 
    def searchForJobs(self, jobTitle):
        self.utility.clickOnElement(Locators.searchBar,15)
        self.driver.find_element_by_xpath(Locators.searchBar).send_keys(jobTitle,Keys.RETURN)
        self.utility.clickOnElement(Locators.jobsButton, 15)
        self.utility.clickOnElement(Locators.experienceLevel,15)
        time.sleep(2)
        self.utility.clickOnElementJs(Locators.entryLevel,15)
        time.sleep(2)
        self.utility.clickOnElementJs(Locators.showResults,15)
        time.sleep(3)


    def clickOnJobs(self):
        f = open("jobData.json", "w")
        jsonObject = "["
        counter = 0

        starting = 1
        ending = len(self.driver.find_elements(By.XPATH, Locators.jobLinks))
   
        while starting != ending:
            jobs = self.driver.find_elements(By.XPATH, Locators.jobLinks)
  
            for x in range (starting -1, ending):
                
                
                jobs[x].click()
                time.sleep(.1)
                
                if(self.indexes_list.count(x) == 0):
                    self.indexes_list.append(x)
                    jsonObject = jsonObject +f"{self.addData(x)}," 
               

                counter+=1
            starting = ending
            ending = len(self.driver.find_elements(By.XPATH, Locators.jobLinks))
 
        jsonObject = jsonObject[:-1]
        jsonObject = jsonObject + "]"

        f.write(jsonObject)
        f.close()

        

    
    def addData(self, x):
        job = Job()
        x= x+1
        
        myStr = "(//ul[@class='jobs-search-results__list list-style-none']/li/div/div/div/div/a/img)[%s]"%(x)
        job.set_title(self.driver.find_element_by_xpath(Locators.title).text)
        job.set_text(self.driver.find_element_by_xpath(Locators.details).text)
        job.set_link(self.driver.find_element_by_xpath(Locators.link).get_attribute('href'))
        job.set_img(self.driver.find_element_by_xpath(myStr).get_attribute('src'))
     
        return job.toJSON()
    
