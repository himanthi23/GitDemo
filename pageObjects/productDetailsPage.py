from selenium.webdriver.common.by import By


class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    addToCart = (By.XPATH, "//div[@class='col-md-12 col-sm-12']//input[2]")
    buyNow = (By.XPATH, "//div[@class='cart']//input[1]")
    inquiryText = (By.XPATH, "//input[@placeholder='Type a message']")
    sendInquiry = (By.CSS_SELECTOR, "input.prd-inq-btn")
    reviewText = (By.LINK_TEXT, "Reviews")

    def getAddToCart(self):
        return self.driver.find_element(*ProductDetailsPage.addToCart)

    def getBuyNow(self):
        return self.driver.find_element(*ProductDetailsPage.buyNow)

    def getInquiryText(self):
        return self.driver.find_element(*ProductDetailsPage.inquiryText)

    def getInquirySend(self):
        return self.driver.find_element(*ProductDetailsPage.sendInquiry)

    def getReviewText(self):
        return self.driver.find_element(*ProductDetailsPage.reviewText)
