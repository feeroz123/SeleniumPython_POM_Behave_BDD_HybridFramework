from behave import *

from features.pages.HomePage import HomePage
from utilities import EmailWithTimestampGenerator


@given(u'I navigate to the Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.select_my_account_option()
    context.register_page = context.home_page.select_register_option()


@when(u'I enter below details into the mandatory fields')
def step_impl(context):
    new_email = EmailWithTimestampGenerator.get_new_email_with_timestamp()

    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["confirm_password"])


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page.select_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_continue_button()


@then(u'Account should get created')
def step_impl(context):
    assert context.account_success_page.verify_account_created_message("Your Account Has Been Created!")


@when(u'I enter below details in all fields')
def step_impl(context):
    new_email = EmailWithTimestampGenerator.get_new_email_with_timestamp()

    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["confirm_password"])
        context.register_page.enter_email(new_email)
        context.register_page.select_newsletter_yes_option()


@when(u'I enter below details in all fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["confirm_password"])
        context.register_page.select_newsletter_yes_option()


@when(u'I enter existing account email into email field')
def step_impl(context):
    context.register_page.enter_email("automation_user@yopmail.com")


@then(u'Proper warning message about duplicate account should be displayed')
def step_impl(context):
    assert context.register_page.verify_email_already_registered_message(
        "Warning: E-Mail Address is already registered!")


@when(u'I do not enter any details in any fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password("")


@then(u'Proper warning message about mandatory fields should be displayed')
def step_impl(context):
    assert context.register_page.verify_agree_privacy_policy_message("Warning: You must agree to the Privacy Policy!")
