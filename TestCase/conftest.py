import pytest
from selenium import webdriver



@pytest.fixture
def setUp():
    driver = webdriver.Chrome('D:\driver\chromedriver_win32\chromedriver.exe')
    return driver