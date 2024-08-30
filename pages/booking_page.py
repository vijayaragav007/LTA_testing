import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.booking_locators import BookingLocators


class TennisBookingCourt(BasePage):
    def __init__(self, driver):
        self.locate = BookingLocators
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

    def play_module(self):
        self.wait_for_element(self.locate.book_a_court).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    
    def hover_over_element(self, element):
        super().hover_over_element(element)

    def checkbox_locate(self,value):
        self.set(self.locate.check_box,value)
        time.sleep(2)

    def check_box_dropdown(self):
        self.click(self.locate.search_drop_button)
        time.sleep(2)

    def click_the_calender(self):
        self.click(self.locate.calender_dropdown)
        time.sleep(2)  

    def hover_over_element(self, element):
        super().hover_over_element(element)
    
    def click_right_arrow_button(self):
        self.click(self.locate.right_click_arrow)
        time.sleep(2)

    def enter_the_date(self):
        self.click(self.locate.enter_date)
        time.sleep(2)

    def time_drop_options(self):
        self.click(self.locate.time_dropdown)
        time.sleep(2)

    def booking_time_slot(self):
        self.click(self.locate.booking_slot)
        time.sleep(2)

    def find_a_court(self):
        self.click(self.locate.click_a_court)
        time.sleep(2)

    def rally_test_one(self):
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        self.click(self.locate.rally_test)
        time.sleep(2)

    def rally_start_time(self):
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        self.click(self.locate.select_start_time)
        time.sleep(2)

    def available_timing(self):
        self.wait_for_element(self.locate.click_a_slot)
        time.sleep(2)

    def test_end_time(self):
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        self.click(self.locate.select_end_time)
        time.sleep(2)

    def click_end_timing(self):
        self.click(self.locate.click_a_end)
        time.sleep(2)

    def find_a_rally_court(self):
        self.click(self.locate.search_a_court)
        time.sleep(2)
    
    def click_outdoor(self):
        self.click(self.locate.outdoor_option)
        time.sleep(2)
    
    def book_a_rally_court(self):
        self.click(self.locate.rally_court)
        time.sleep(2)
    
   

    
    

    