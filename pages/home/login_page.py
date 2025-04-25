from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Locators
        self._login_link = "//a[text()='Sign In']"
        self._email_field = "//form[@name = 'loginform']//input[@id='email']"
        self._password_field = "//form[@name = 'loginform']//input[@id='login-password']"
        self._login_button = "login"
    
    #Define elements' actions method
    def click_login_link(self):
        self.click_element(self._login_link, "xpath")

    def enter_email_address(self, email):
        self.send_values(email, self._email_field, "xpath")
    
    def enter_password(self, password):
        self.send_values(password, self._password_field, "xpath")
    
    def click_login_button(self):
        self.click_element(self._login_button, "id")
    
    def login(self, email="", password=""):
        self.click_login_link()
        self.enter_email_address(email=email)
        self.enter_password(password=password)
        self.click_login_button()

    def verify_successful_login(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']//span[text()='My Account']", "xpath")
        return result
    def verify_faild_login(self):
        result = self.isElementPresent("incorrectdetails", "id")
        return result
    def verify_homepage_title(self):
        return self.verifyPageTitle("Login")
