from datetime import datetime

from behave import *

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to the Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.home_page.click_register_option()


@when(u'I enter mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)

    time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    new_email = "test_user_" + time_stamp + "@yopmail.com"

    context.register_page.enter_first_name("Test")
    context.register_page.enter_last_name("User")
    context.register_page.enter_email(new_email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm_password("12345")


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.select_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_continue_button()


@then(u'Account should get created')
def step_impl(context):
    context.account_success_page = AccountSuccessPage(context.driver)

    expected_text = "Your Account Has Been Created!"
    assert context.account_success_page.verify_account_created_message(expected_text)


@when(u'I enter details in all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    new_email = "test_user_" + time_stamp + "@yopmail.com"

    context.register_page.enter_first_name("Test")
    context.register_page.enter_last_name("User")
    context.register_page.enter_email(new_email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm_password("12345")
    context.register_page.select_newsletter_yes_option()


@when(u'I enter details in all fields except email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("Test")
    context.register_page.enter_last_name("User")
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm_password("12345")
    context.register_page.select_newsletter_yes_option()


@when(u'I enter existing account email into email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_email("automation_user@yopmail.com")


@then(u'Proper warning message about duplicate account should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)

    expected_message = "Warning: E-Mail Address is already registered!"
    assert context.register_page.verify_email_already_registered_message(expected_message)


@when(u'I do not enter any details in any fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email()
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password("")


@then(u'Proper warning message about mandatory fields should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    expected_message = "Warning: You must agree to the Privacy Policy!"
    assert context.register_page.verify_agree_privacy_policy_message(expected_message)
