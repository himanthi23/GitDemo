from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # logoutLinkTextValue = "Log Out"
    loginText = (By.LINK_TEXT, "Login | Signup")
    logoutText = (By.LINK_TEXT, "Log Out")
    topSearch = (By.ID, "common-search-input")
    searchButton = (By.XPATH, "//button[@name='submit_search']")
    category = (By.XPATH, "//div[contains(text(),'Categories')]")
    mainCategory = (By.CSS_SELECTOR, "li.item-vertical")
    subCategory = (By.CSS_SELECTOR, "a.main-menu")
    catLinkText = (By.CSS_SELECTOR, "ul.mer-bc-list")
    products = (By.XPATH, "//div[@class='product-item-container product-grid4']")
    productTitles = (By.XPATH, "//div//div/div//div//div//div//div//div//h4")
    searchProductTitles = (By.XPATH, "//div[@class='products-category']//div//div//div//div//div//div//div//div//h4")
    addToCart = (By.CSS_SELECTOR, "i.fa-shopping-cart")
    myCart = (By.XPATH, "//button[contains(text(),'MY CART')]")
    noItemsFound = (By.XPATH, "//h4[contains(text(),'No Items Found')]")
    breadcrumb = (By.XPATH, "//ul[@class='breadcrumb mer-bc-list']")
    breadcrumbText = (By.XPATH, "//ul[@class='breadcrumb mer-bc-list']//a")

    # Product Quick View
    ProductImagePQV = (By.CSS_SELECTOR, ".large-image")
    QtyPlusPQV = (By.XPATH, "//div[contains(text(),'+')]")
    AddToCartPQV = (By.XPATH, "//div[@class='cart']//input[2]")
    CartItemCount = (By.XPATH, "//span[@class='items_cart']")
    ShoppingCartDropdown = (By.XPATH, "//ul[@class='dropdown-menu pull-right shoppingcart-box cart-dropdown']")


    # def getloginSignup(self):
    #     return self.driver.find_element(*HomePage.loginSignup)

    def getLoginText(self):
        return self.driver.find_element(*HomePage.loginText)

    def getLogoutText(self):
        return self.driver.find_element(*HomePage.logoutText)

    def getTopSearch(self):
        return self.driver.find_element(*HomePage.topSearch)

    def getSearchButton(self):
        return self.driver.find_element(*HomePage.searchButton)

    def getCategory(self):
        return self.driver.find_element(*HomePage.category)

    def getMainCategory(self):
        return self.driver.find_elements(*HomePage.mainCategory)

    def getSubCategory(self):
        return self.driver.find_elements(*HomePage.subCategory)

    def getAddToCart(self):
        return self.driver.find_elements(*HomePage.addToCart)

    def getProducts(self):
        return self.driver.find_elements(*HomePage.products)

    def getProductTitles(self):
        return self.driver.find_elements(*HomePage.productTitles)

    def getSearchProductTitles(self):
        return self.driver.find_elements(*HomePage.searchProductTitles)

    def getViewCart(self):
        return self.driver.find_elements(*HomePage.myCart)

    def getNoItemsFound(self):
        return self.driver.find_element(*HomePage.noItemsFound)

    def isNoItemsFound(self):
        try:
            self.driver.find_element(*HomePage.noItemsFound)
            return True
        except NoSuchElementException:
            return False

    def getBreadcrumb(self):
        return self.driver.find_element(*HomePage.breadcrumb)

    def getBreadcrumbText(self):
        temp_elements = self.driver.find_elements(*HomePage.breadcrumbText)

        temp_text = ""
        for ele in temp_elements:
            temp_text = temp_text + ele.text + " "

        return temp_text

    def getAddToCartPQV(self):
        return self.driver.find_element(*HomePage.AddToCartPQV)

    def getQtyPlusPQV(self):
        return self.driver.find_element(*HomePage.QtyPlusPQV)

    def getMyCartButton(self):
        return self.driver.find_element(*HomePage.myCart)

    def getCartItemCount(self):
        return self.driver.find_element(*HomePage.CartItemCount)

    def getShoppingCartDropdown(self):
        return self.driver.find_element(*HomePage.ShoppingCartDropdown)

    def getSubCategoryLinksElement(self, parentCategoryText):
        sub_category_links_xpath = "//ul[@class='megamenu']/li//span[contains(text(),'{}')]/ancestor::li//div[@class='sub-menu']//div[@class='col-md-12 static-menu']//a".format(
            parentCategoryText)
        return (By.XPATH, sub_category_links_xpath)

    def getSubCategoryLinks(self, parentCategoryText):
        return self.driver.find_elements(*HomePage.getSubCategoryLinksElement(self, parentCategoryText))

