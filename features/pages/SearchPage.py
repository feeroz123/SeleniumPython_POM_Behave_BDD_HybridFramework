from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    valid_product_link_text = "HP LP3065"
    incorrect_message_xpath = "//input[@id='button-search']//following-sibling::p"

    def verify_valid_product_displayed(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_product_link_text).is_displayed()

    def verify_incorrect_message_displayed(self, expected_text):
        return self.driver.find_element(By.XPATH, self.incorrect_message_xpath).text.__eq__(expected_text)