from hashlib import new
import pytest
from selenium import webdriver
from utilities.test_data import TestData


@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    # elif request.param == "edge":
    #     driver = webdriver.Edge()
    # elif request.param == "firefox":
    #     driver = webdriver.Firefox()
    request.cls.driver = driver
    print("Browser:", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()
