from pages.lta_search_logo import LTASearchPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestSearchLogin(BaseTest):
    def test_search_page(self):  
        lta_search_page= LTASearchPage(self.driver)
        lta_search_page.lta_username(TestData.Username)
        lta_search_page.lta_password(TestData.Password)
        lta_search_page.click_lta_login()
        lta_search_page.Accept_all_cookies()       
        element = lta_search_page.find_element(*lta_search_page.locate.title_of_compete)
        lta_search_page.hover_over_element(element)
        lta_search_page.the_compete_module()
        lta_search_page.all_youth_competitons()
        # lta_search_page.click_lta_youth_tour()
        