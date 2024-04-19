from features.pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_created_message_xpath = "//div[@id='content']/h1"

    def verify_account_created_message(self, expected_message):
        return self.verify_element_text("account_created_message_xpath", self.account_created_message_xpath,
                                        expected_message)
