from pages.base_page import BasePage
import time
from utilities.search_module_locators import SearchLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



class LTASearchPage(BasePage):
    def __init__(self, driver):
        self.locate = SearchLocators
        self.actions = ActionChains(driver)
        super().__init__(driver)

    def lta_username(self, lta_username):
        self.set(self.locate.Username, lta_username)

    def lta_password(self, lta_password):
        self.set(self.locate.Password, lta_password)

    def click_lta_login(self):
        self.click(self.locate.Verify_button)
        time.sleep(2)

    def Accept_all_cookies(self):
        self.wait_for_element(self.locate.all_cookies).click()
        time.sleep(2)

    def hover_over_element(self, element):
        super().hover_over_element(element)    

    def the_compete_module(self):
        self.wait_for_element(self.locate.junior_option).click()
        time.sleep(2)
    
    def all_youth_competitons(self):
        self.scroll_to_element(self.locate.click_all_youth_option)
        self.wait_and_click(self.locate.click_all_youth_option)
        

    # def click_lta_youth_tour(self):
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()
    #     self.wait_for_element(self.locate.local_tour).click()
    #     time.sleep(2)
    

    