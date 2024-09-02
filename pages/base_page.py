from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



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
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(value)
        
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
    
    def scroll_to_element(self, locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    

    def wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    



# def wait_and_click(self, locator):
#     element = WebDriverWait(self.driver, 10).until(
#         EC.element_to_be_clickable(locator)
#     )
#     element.click()

# def scroll_to_element(self, locator):
#     element = WebDriverWait(self.driver, 10).until(
#         EC.presence_of_element_located(locator)
#     )
#     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

# def safe_click(self, locator):
#     element = WebDriverWait(self.driver, 10).until(
#         EC.element_to_be_clickable(locator)
#     )
#     try:
#         element.click()
#     except StaleElementReferenceException:
#         element = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(locator)
#         )
#         element.click()

#     def js_click(self, locator):
#         element = WebDriverWait(self.driver, 10).until(
#         EC.element_to_be_clickable(locator)
#     )
#     self.driver.execute_script("arguments[0].click();", element)

#     def click_with_delay(self, locator, delay=2):
#         WebDriverWait(self.driver, 10).until(
#         EC.element_to_be_clickable(locator)
#     )
#         time.sleep(delay)
#         self.click(locator)
    
#     def handle_alert(self):
#         try:
#             WebDriverWait(self.driver, 5).until(EC.alert_is_present())
#             alert = Alert(self.driver)
#             alert.accept()
#         except TimeoutException:
#             pass

        
        
