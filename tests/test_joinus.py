from pages.joinus_page import ADEJoinUs
from tests.base_test import BaseTest
from utilities.test_data import TestData




class Testjoinuspage(BaseTest):
    def test_joinus_page(self):  
        ade_joinus_page= ADEJoinUs(self.driver)
        ade_joinus_page.ade_username(TestData.Username)
        ade_joinus_page.ade_password(TestData.Password)
        ade_joinus_page.click_ade_login()
        ade_joinus_page.Accept_all_cookies()
        ade_joinus_page.click_on_joinus()
        ade_joinus_page.enter_the_joinnow()
        ade_joinus_page.joinnow_first_name("vijay")
        ade_joinus_page.now_last_name("vr")
        ade_joinus_page.enter_the_date("08")
        ade_joinus_page.enter_the_month("06")
        ade_joinus_page.enter_the_year("1995")
        ade_joinus_page.click_on_the_gender()
        ade_joinus_page.enter_the_email("vijay.jayaraman@verolt.com")
        ade_joinus_page.create_a_username("Vijay086")
        ade_joinus_page.create_a_password("Vijayverolt@123")
        ade_joinus_page.click_robot_button()
        ade_joinus_page.click_join_now_button()