from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

#src/pages

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    #TC-002 Successful Login
    @pytest.mark.run(order = 2)
    def test_valid_login(self):
        self.login_page.login("Test@email.com", "abcabc")
        
        result1 = self.login_page.verify_homepage_title()
        print("=="*30) 
        print("Point 1: Verifying the page title, title is:" + str(result1))
        self.ts.mark(result1, "The Title is incorrect")
        result2 = self.login_page.verify_successful_login()
        print("Point 2: Verifying the Login, title is: the login " + str(result2))
        self.ts.markFinal("Test Login", result2, "Login was not successfull")
        
        
    #TC-001 Failed Login
    @pytest.mark.run(order = 1)
    def test_invalid_login(self):
        self.login_page.login("est@email.com", "abcabcZZZ")
        result = self.login_page.verify_faild_login()
        assert result is True
