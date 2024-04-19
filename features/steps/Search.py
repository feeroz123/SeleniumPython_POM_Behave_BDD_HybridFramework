from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'Navigate to the Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)

    expected_title = "Your Store"
    assert context.home_page.check_home_page_title(expected_title)


@when(u'I enter a valid product in the Search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_search_field_value("HP")


@when(u'I click on Search button')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_search_button()


@then(u'Valid product should get displayed in the search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.verify_valid_product_displayed()


@when(u'I enter an invalid product in the Search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_search_field_value("Honda")


@then(u'Proper message should be displayed in the search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)

    expected_text = "There is no product that matches the search criteria."
    assert context.search_page.verify_incorrect_message_displayed(expected_text)


@when(u'I do not enter anything in the Search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_search_field_value("")
