from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # forgotPasswordLinkTextValue = "Forgot Password ?"

    email = (By.CSS_SELECTOR, "#text")
    password = (By.CSS_SELECTOR, "#pwd")
    login = (By.CSS_SELECTOR, "#btnlogin")

    def getemail(self):
        return self.driver.find_element(*LoginPage.email)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.login)
