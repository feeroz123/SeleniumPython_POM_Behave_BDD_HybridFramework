# Before Scenario hook
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context, driver):
    browser = ConfigReader.read_configuration("basic info", "browser")

    if browser.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        context.driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()

    url = ConfigReader.read_configuration("basic info", "url")
    context.driver.get(url)


# After Scenario hook
def after_scenario(context, driver):
    context.driver.quit()


# To take screenshot for failed test steps
def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot", attachment_type=AttachmentType.PNG)
