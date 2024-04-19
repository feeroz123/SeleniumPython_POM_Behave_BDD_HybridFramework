from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    # Action methods
    def select_my_account_option(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        return RegisterPage(self.driver)

    def check_home_page_title(self, expected_title):
        return self.verify_page_title(expected_title)

    def enter_search_field_value(self, search_text):
        self.type_into_element("search_box_field_name", self.search_box_field_name, search_text)

    def click_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)

