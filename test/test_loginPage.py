import unittest

import pytest

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from testData.loginPageData import loginPageData
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    @pytest.mark.dependency(name="login")
    #@pytest.mark.first
    def test_loginSubmission(self, getData):
        # Get logger
        log = self.getLogger()
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        # Click login signup link
        home.getLoginText().click()
        # Wait until login modal appears
        self.verifyLinkPresence("Forgot Password ?")

        # Enter email and password
        log.info("Email or Mobile no is" + getData["email"])
        login.getemail().send_keys(getData["email"])
        log.info("Password is" + getData["password"])
        login.getpassword().send_keys(getData["password"])
        login.getLoginButton().click()
        # Wait until Log Out link appears
        self.verifyLinkClickable("//b[contains(text(),'Log Out')]")
        #self.driver.implicitly_wait(10)
        # Assert Log Out link
        logoutText = home.getLogoutText().text
        log.info("text received from Logout button is" + logoutText)
        assert ("Log Out" in logoutText)
        self.driver.refresh()

    @pytest.fixture(params=loginPageData.test_loginPageData)
    def getData(self, request):
        return request.param

    @pytest.mark.dependency(name="logout", depends=["login"])
    #@pytest.mark.last
    def test_logoutSubmission(self):
        log = self.getLogger()
        home = HomePage(self.driver)
        home.getLogoutText().click()
        self.verifyLinkPresence("Login | Signup")
        loginText = home.getLoginText().text
        log.info("text received from Login button is" + loginText)
        assert ("Login | Signup" in loginText)
