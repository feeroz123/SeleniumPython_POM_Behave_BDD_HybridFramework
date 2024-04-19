from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    my_account_option = "//span[text()='My Account']"
    login_option = "Login"
    register_option = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    # Action methods
    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_option).click()

    def click_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option).click()

    def click_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option).click()

    def check_home_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def enter_search_field_value(self, search_text):
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(search_text)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

