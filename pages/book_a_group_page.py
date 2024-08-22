import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.book_group_locators import BookGroupLocators




class BookGroupLesson(BasePage):
    def __init__(self, driver):
        self.locate = BookGroupLocators
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

    def play_module(self):
        self.wait_for_element(self.locate.book_a_group).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(10)
    
    def hover_over_element(self, element):
        super().hover_over_element(element)
    
    def group_lesson_checkbox(self,value):
        self.set(self.locate.group_check_box,value)
        time.sleep(2)
    
    def group_lesson_dropdown(self):
        self.click(self.locate.group_lesson_drops)
        time.sleep(2)

    def find_a_court(self):
        self.click(self.locate.find_a_class)
        time.sleep(2)

    def AA_Custom_recurring(self):
        self.wait_for_element(self.locate.Custom_recurring).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)    

    # def Custom_Recurring_checkbox(self):
    #     self.click(self.locate.Custom_recurring_checkbox)
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()
    #     time.sleep(2)

    # def Book_a_Custom_recurring(self):
    #     self.wait_for_element(self.locate.book_a_custom_class).click()
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()
    #     time.sleep(2)

    # def group_session_book_class(self):
    #     self.click(self.locate.book_a_class)
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()
    #     time.sleep(2)

    