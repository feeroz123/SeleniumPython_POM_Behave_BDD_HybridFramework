from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    newsletter_yes_field_xpath = "//input[@name='newsletter' and @value=1]"
    newsletter_no_field_xpath = "//input[@name='newsletter' and @value=2]"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[contains(@class, 'alert')]"
    privacy_policy_option_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    email_already_registered_message_xpath = "//div[contains(@class, 'alert')]"
    agree_privacy_policy_message_xpath = "//div[contains(@class, 'alert')]"

    def enter_first_name(self, first_name):
        self.type_into_element("first_name_field_id", self.first_name_field_id, first_name)

    def enter_last_name(self, last_name):
        self.type_into_element("last_name_field_id", self.last_name_field_id, last_name)

    def enter_email(self, email):
        self.type_into_element("email_field_id", self.email_field_id, email)

    def enter_telephone(self, phone):
        self.type_into_element("telephone_field_id", self.telephone_field_id, phone)

    def enter_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def enter_confirm_password(self, confirm_password):
        self.type_into_element("confirm_password_field_id", self.confirm_password_field_id, confirm_password)

    def select_newsletter_yes_option(self):
        self.click_on_element("newsletter_yes_field_xpath", self.newsletter_yes_field_xpath)

    def select_newsletter_no_option(self):
        self.click_on_element("newsletter_no_field_xpath", self.newsletter_no_field_xpath)

    def click_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def verify_warning_message(self, expected_message):
        return self.verify_element_text("warning_message_xpath", self.warning_message_xpath, expected_message)

    def select_privacy_policy(self):
        self.click_on_element("privacy_policy_option_name", self.privacy_policy_option_name)

    def click_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def verify_email_already_registered_message(self, expected_message):
        return self.verify_element_text("email_already_registered_message_xpath",
                                        self.email_already_registered_message_xpath, expected_message)

    def verify_agree_privacy_policy_message(self, expected_message):
        return self.verify_element_text("agree_privacy_policy_message_xpath", self.agree_privacy_policy_message_xpath,
                                        expected_message)
