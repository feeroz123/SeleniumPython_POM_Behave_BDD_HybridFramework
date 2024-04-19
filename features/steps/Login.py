from behave import *

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I am on the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.home_page.click_login_option()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("automation_user@yopmail.com")
    context.login_page.enter_password("Automation123")


@when(u'I click on the login button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_login_button()


@then(u'I should get logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_your_account_info_option()


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("invalid_user@yopmail.com")
    context.login_page.enter_password("Automation123")


@then(u'I should get a proper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.verify_warning_message_displayed(expected_warning_message)


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("automation_user@yopmail.com")
    context.login_page.enter_password("InvalidPassword")


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("invalid_user@yopmail.com")
    context.login_page.enter_password("InvalidPassword")


@when(u'I do not enter any credentials')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
