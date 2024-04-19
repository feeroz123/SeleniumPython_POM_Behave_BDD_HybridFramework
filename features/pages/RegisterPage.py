from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    newsletter_yes_field_id = "//input[@name='newsletter' and @value=1]"
    newsletter_no_field_id = "//input[@name='newsletter' and @value=2]"
    login_button_xpath = "//input[@value='Login']"
    warning_message = "//div[contains(@class, 'alert')]"
    privacy_policy_option_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    email_already_registered_message_path = "//div[contains(@class, 'alert')]"
    agree_privacy_policy_message_xpath = "Warning: You must agree to the Privacy Policy!"


    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_telephone(self, phone):
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password)

    def select_newsletter_yes_option(self):
        self.driver.find_element(By.XPATH, self.newsletter_yes_field_id).click()

    def select_newsletter_no_option(self):
        self.driver.find_element(By.XPATH, self.newsletter_no_field_id).click()

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def verify_warning_message(self, expected_message):
        return self.driver.find_element(By.XPATH, self.warning_message).text.__contains__(expected_message)

    def select_privacy_policy(self):
        self.driver.find_element(By.NAME, self.privacy_policy_option_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def verify_email_already_registered_message(self, expected_message):
        return self.driver.find_element(By.XPATH, self.email_already_registered_message_path).text.__contains__(expected_message)

    def verify_agree_privacy_policy_message(self, expected_message):
        return self.driver.find_element(By.XPATH, self.agree_privacy_policy_message_xpath).text.__contains__(expected_message)


