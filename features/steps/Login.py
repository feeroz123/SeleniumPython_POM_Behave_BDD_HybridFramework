from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("automation_user@yopmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("Automation123")


@when(u'I click on the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I should get logged in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    context.driver.quit()


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("invalid_user@yopmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("Automation123")


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    print("ACTUAL:" + context.driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]").text)
    assert (context.driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]").text
            .__contains__(expected_warning_message))
    context.driver.quit()


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("automation_user@yopmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("InvalidPassword")


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("invalid_user@yopmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("InvalidPassword")


@when(u'I do not enter any credentials')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
