from features.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_info_option_link_text = "Edit your account information"

    def display_status_of_edit_your_account_info_option(self):
        return self.verify_element_display("edit_your_account_info_option_link_text",
                                           self.edit_your_account_info_option_link_text)
