from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "HP LP3065"
    incorrect_message_xpath = "//input[@id='button-search']//following-sibling::p"

    def verify_valid_product_displayed(self):
        return self.verify_element_display("valid_product_link_text", self.valid_product_link_text)

    def verify_incorrect_message_displayed(self, expected_text):
        return self.verify_element_text("incorrect_message_xpath", self.incorrect_message_xpath, expected_text)
