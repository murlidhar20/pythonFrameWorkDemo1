print("printer")

from selenium import webdriver
from TestCase.conftest import setUp
from BasePage.BasePage import BasePage
from PageObject.LoginPage import LoginPage





class Test001:
    def test_divisible_by_3(self, setUp):
        print("Login the application---------------------")
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self._basePage = BasePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.loginPage("admin@yourstore.com", "admin")
        self._basePage.closeBrowser()
