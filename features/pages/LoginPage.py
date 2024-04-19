from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[contains(@class, 'alert')]"

    def enter_email_address(self, email_address):
        self.type_into_element("email_address_field_id", self.email_address_field_id, email_address)

    def enter_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def click_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def verify_warning_message_displayed(self, message):
        return self.verify_element_text("warning_message_xpath", self.warning_message_xpath, message)
