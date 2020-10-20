from selenium.webdriver.common.by import By


class CheckOutPagePage:
    def __init__(self, driver):
        self.driver = driver

    proceed = (By.XPATH, "//button[contains(text(),'Proceed To Checkout')]")
    delete = (By.CSS_SELECTOR, "button.btn-danger")
    increaseDecreaseQty = (By.CSS_SELECTOR, ".input-group-addon")
    totalWeight = (By.CSS_SELECTOR, "#weightDiv")
    minOrderLabel = (By.XPATH, "//b[contains(text(),'Minimum Cart Value Rs.500. Please Add More Items.')]")
    paymentOptions = (By.CSS_SELECTOR, "div.square-contents")
    paymentProceed = (By.XPATH, "//div[@class='modal-body']//div[@class='row']//div[@class='row']//button[@class='btn proceed-btn'][contains(text(),'Proceed')]")

    def getProceedToCheckOut(self):
        return self.driver.find_element(*CheckOutPagePage.proceed)

    def getDeleteProducts(self):
        return self.driver.find_elements(*CheckOutPagePage.delete)

    def getChangeQty(self):
        return self.driver.find_elements(*CheckOutPagePage.increaseDecreaseQty)

    def getTotalWeight(self):
        return self.driver.find_element(*CheckOutPagePage.totalWeight)

    def getMinOrderlabel(self):
        return self.driver.find_element(*CheckOutPagePage.minOrderLabel)

    def getPaymentOptions(self):
        return self.driver.find_elements(*CheckOutPagePage.paymentOptions)

    def getPaymentProceed(self):
        return self.driver.find_elements(*CheckOutPagePage.paymentProceed)