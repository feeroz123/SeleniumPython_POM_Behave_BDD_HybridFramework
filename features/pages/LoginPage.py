from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message = "//div[contains(@class, 'alert')]"

    def enter_email_address(self, email_address):
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def verify_warning_message_displayed(self, message):
        return self.driver.find_element(By.XPATH, self.warning_message).text.__contains__(message)
