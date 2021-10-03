
class Locators:

    # loginPage 
    usernameField_xpath = "//input[@name='session_key']"
    passwordField_xpath = "//input[@id='session_password']"
    signIn_xpath = "//button[@class='sign-in-form__submit-button']"

    #mainPage
    searchBar = "//input[@placeholder='Search']"
    jobsButton = "//button[text()='Jobs']"
    experienceLevel = "//button[text()='Experience Level']"
    entryLevel = "//span[text()='Entry level']"
    showResults = "(//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml2'])[2]"
    jobLinks = "//ul[@class='jobs-search-results__list list-style-none']/li/div/div"
    title = "//a[@class='ember-view']/h2[@class='t-16 t-black t-bold truncate']"
    details = "//div[@id='job-details']"
    link = "//h2[@class='t-24 t-bold']/.."
