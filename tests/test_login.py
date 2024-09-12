from pages.lta_login_page import LTAHomePage
from tests.base_test import BaseTest
from utilities.test_data import TestData
from selenium.webdriver.common.by import By


class TestLogin(BaseTest):

    def test_lta_login(self):
        lta_home_page = LTAHomePage(self.driver)
        lta_home_page.lta_username(TestData.Username)
        lta_home_page.lta_password(TestData.Password)
        lta_home_page.click_lta_login()
        lta_home_page.Accept_all_cookies()    
        # element = lta_home_page.find_element(*lta_home_page.locate.compete)
        lta_home_page.hover_over_element(element)
        lta_home_page.compete_module() 
        lta_home_page.junior_module()
        lta_home_page.compete_module()
        lta_home_page.LTA_Youth_Competitions()
        lta_home_page.individual_match_competition()
        element = lta_home_page.find_element(*lta_home_page.locate.submit_lta)
        lta_home_page.hover_over_element(element)
        lta_home_page.enter_a_LTA()
        lta_home_page.lta_tennis_privacy()
        lta_home_page.tournaments_module()
        lta_home_page.search_tournaments()
        lta_home_page.leamington_lta_youth()
        lta_home_page.enter_leamington_lta()

        