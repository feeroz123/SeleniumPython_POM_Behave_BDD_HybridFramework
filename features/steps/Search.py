from behave import *

from features.pages.HomePage import HomePage


@given(u'Navigate to the Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title("Your Store")


@when(u'I enter a valid product as "{product}" in the Search box')
def step_impl(context, product):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_search_field_value(product)


@when(u'I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_search_button()


@then(u'Valid product should get displayed in the search results')
def step_impl(context):
    assert context.search_page.verify_valid_product_displayed()


@when(u'I enter an invalid product as "{product}" in the Search box')
def step_impl(context, product):
    context.home_page.enter_search_field_value(product)


@then(u'Proper message should be displayed in the search results')
def step_impl(context):
    assert context.search_page.verify_incorrect_message_displayed(
        "There is no product that matches the search criteria.")


@when(u'I do not enter anything in the Search box')
def step_impl(context):
    context.home_page.enter_search_field_value("")
