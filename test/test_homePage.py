import random

import pytest
from selenium.webdriver import ActionChains

from pageObjects.checkOutPage import CheckOutPagePage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.productDetailsPage import ProductDetailsPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    # @pytest.mark.second_to_last
    # @pytest.mark.dependency(name="search", depends=["login"])
    def test_SearchProducts(self):
        log = self.getLogger()
        home = HomePage(self.driver)

        searchText = "milk"
        home.getTopSearch().send_keys(searchText)
        home.getSearchButton().click()
        self.verifyAllLinkPresence("//div[@class='product-item-container product-grid4']")
        productsList = home.getSearchProductTitles()

        for productLink in productsList:
            log.info("Product Link Test Found: " + productLink.text)
            assert (searchText.casefold() in productLink.text.casefold())

    def test_addToCart(self):
        log = self.getLogger()
        home = HomePage(self.driver)
        products = ProductDetailsPage(self.driver)
        checkout = CheckOutPagePage(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(home.getCategory()).perform()
        mainCatList = home.getMainCategory()
        # count = len(cat1List)

        # level1category = 11
        # for cat1 in cat1List:
        #     log.info("Category 1 list Found : " + cat1.text)
        #     assert count == level1category
        log.info("Main Category is : " + mainCatList[0].text)
        action.move_to_element(mainCatList[0]).perform()
        subCatList = home.getSubCategory()
        log.info("Sub Category is : " + subCatList[1].text)
        action.move_to_element(subCatList[1]).click().perform()
        self.verifyAllLinkPresence("//div[9]")



    def selectRandomSubCategory(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        action = ActionChains(self.driver)
        category_links = home_page.getMainCategory()

        category_links_len = len(category_links)
        random_category_index = random.randint(0, (category_links_len - 2))

        if random_category_index == (category_links_len - 2):
            first_category = category_links[random_category_index - 1]
            second_category = category_links[random_category_index]
        else:
            first_category = category_links[random_category_index]
            second_category = category_links[random_category_index + 1]

        TestHomePage.main_category = first_category.text

        action.move_to_element(first_category).perform()

        self.verifyLinkPresenceByCss(home_page.getSubCategory().text)

        sub_category_links = home_page.getSubCategoryLinks(first_category.text)
        sub_category_links_len = len(sub_category_links)
        random_sub_category_index = random.randint(0, (sub_category_links_len - 1))

        ran_sub_category = sub_category_links[random_sub_category_index]
        TestHomePage.sub_category = ran_sub_category.text

        ActionChains(self.driver).click(ran_sub_category).perform()

        log.info(TestHomePage.main_category)
        log.info(TestHomePage.sub_category)
