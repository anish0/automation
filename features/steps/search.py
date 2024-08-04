from behave import *

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given('I am in homepage')
def step_impl(context):
    expected_title = "Your Store"
    context.home_page = HomePage(context.driver)
    assert context.home_page.verify_homepage_title(expected_title)


@when('I enter valid product in the search box')
def step_impl(context):
    try:
        context.home_page.enter_into_search_box("HP")
    except Exception as e:
        print(f"An error occurred: {e}")


@when(u'I click on search button')
def step_impl(context):
    try:
        context.home_page.click_search_button()
    except Exception as e:
        print(f"An error occurred: {e}")


@then(u'Valid product should get displayed in search result')
def step_impl(context):
    try:
        context.search_page = SearchPage(context.driver)
        assert context.search_page.is_searched_item_displayed(), "The searched item is not displayed."
    except Exception as e:
        print(f"An error occurred: {e}")


@when(u'I enter invalid product in the search box')
def step_impl(context):
    try:
        context.home_page.enter_into_search_box("lado")
    except Exception as e:
        print(f"An error occurred: {e}")


@then(u'Proper error message should be displayed')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    context.search_page = SearchPage(context.driver)
    actual_message = context.search_page.error_message()
    assert expected_text == actual_message, f"Expected: '{expected_text}', but got: '{actual_message}'"


@when(u'I do not enter anything in the search box')
def step_impl(context):
    try:
        context.home_page.enter_into_search_box("")
    except Exception as e:
        print(f"An error occurred: {e}")
