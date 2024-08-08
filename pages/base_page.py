from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException





class BasePage:
    """
    The Purpose Of A Basepage Is To Contain Methods Common To All Page Objects
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))
    
    def hover_over_element(self, element): 
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        
    
       
    
        
    
    

    
    
    