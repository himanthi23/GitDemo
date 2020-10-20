from selenium.webdriver.common.by import By


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    personalTab = (By.XPATH, "//li[@class='active']//a[contains(text(),'Personal')]")
    address = (By.XPATH, "//a[contains(text(),'Addresses')]")
    changePassword = (By.XPATH, "//a[contains(text(),'Change Password')]")
    entitlements = (By.XPATH, "//a[contains(text(),'Entitlements')]")
    firstName = (By.XPATH, "//input[@placeholder='First Name']")
    middleName = (By.XPATH, "// input[ @ placeholder = 'Middle Name']")
    lastName = (By.XPATH, "//input[@placeholder='Last Name']")
    dob = (By.XPATH, "//input[@placeholder='Select Date']")
    gender = (By.XPATH, "//select[@id='genderSelect']")
    homeNumber = (By.XPATH, "//input[@id='mobileInput-26_phone_number']")
    submit = (By.XPATH, "//div[@class='col-lg-12']//button[@class='btn buyerprof-sbtn'][contains(text(),'Submit')]")
    upload = (By.XPATH, "//button[@class='btn btn-sm buyerprof-sbtn profupload-btn']")


    def personalData(self):
        return self.driver.find_element(*ProfilePage.personalTab)

    def address(self):
        return self.driver.find_element(*ProfilePage.address)

    def PassowordChange(self):
        return self.driver.find_element(*ProfilePage.changePassword)

    def entitlements(self):
        return self.driver.find_element(*ProfilePage.entitlements)

    def firstName(self):
        return self.driver.find_element(*ProfilePage.firstName)

    def middleName(self):
        return self.driver.find_element(*ProfilePage.middleName)

    def lastName(self):
        return self.driver.find_element(*ProfilePage.lastName)

    def dob(self):
        return self.driver.find_element(*ProfilePage.dob)

    def gender(self):
        return self.driver.find_element(*ProfilePage.gender)

    def homeNumber(self):
        return self.driver.find_element(*ProfilePage.homeNumber)

    def submit(self):
        return self.driver.find_element(*ProfilePage.submit)

    def uUpload(self):
        return self.driver.find_element(*ProfilePage.upload)

