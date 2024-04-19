from behave import *

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I am on the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.select_my_account_option()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("automation_user@yopmail.com")
    context.login_page.enter_password("Automation123")


@when(u'I click on the login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_info_option()


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("invalid_user@yopmail.com")
    context.login_page.enter_password("Automation123")


@then(u'I should get a proper warning message')
def step_impl(context):
    assert context.login_page.verify_warning_message_displayed("Warning: No match for E-Mail Address and/or Password.")


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("automation_user@yopmail.com")
    context.login_page.enter_password("InvalidPassword")


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("invalid_user@yopmail.com")
    context.login_page.enter_password("InvalidPassword")


@when(u'I do not enter any credentials')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
