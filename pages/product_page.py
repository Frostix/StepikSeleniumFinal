from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_login_url()
        self.should_add_to_cart()
        self.should_be_register_form()
        self.add_to_cart()
        self.should_be_correct_product()
        self.should_be_correct_price()
        

    def should_be_login_url(self):
        assert "login" in self.browser.current_url , "Login is not in URL"

    def should_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add to cart button is not presented"

    def add_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        btn.click()

    def should_be_correct_product(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT).text
                    == self.browser.find_element(*ProductPageLocators.PRODUCT_ALLERT).text), "Product allert is not correct"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text in self.browser.find_element(*ProductPageLocators.PRICE_ALLERT).text, "Price is not correct"
        
   