from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigate to the Register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@when(u'I enter mandatory fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    new_email = "test_user_" + time_stamp + "@yopmail.com"

    context.driver.find_element(By.ID, "input-firstname").send_keys("Test")
    context.driver.find_element(By.ID, "input-lastname").send_keys("User")
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)
    context.driver.quit()


@when(u'I enter details in all fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    new_email = "test_user_" + time_stamp + "@yopmail.com"

    context.driver.find_element(By.ID, "input-firstname").send_keys("Test")
    context.driver.find_element(By.ID, "input-lastname").send_keys("User")
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter' and @value=1]").click()


@when(u'I enter details in all fields except email field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Test")
    context.driver.find_element(By.ID, "input-lastname").send_keys("User")
    context.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter' and @value=1]").click()


@when(u'I enter existing account email into email field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("automation_user@yopmail.com")


@then(u'Proper warning message about duplicate account should be displayed')
def step_impl(context):
    expected_message = "Warning: E-Mail Address is already registered!"
    assert (context.driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]")
            .text.__contains__(expected_message))
    context.driver.quit()


@when(u'I do not enter any details in any fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys()
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then(u'Proper warning message about mandatory fields should be displayed')
def step_impl(context):
    expected_message = "Warning: You must agree to the Privacy Policy!"
    assert (context.driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]")
            .text.__contains__(expected_message))
    context.driver.quit()
