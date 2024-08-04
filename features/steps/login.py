from behave import *
from selenium.webdriver.common.by import By
from datetime import datetime

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I am in login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_login_option()


@when(u'I enter valid email address and password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("fakeemail@gmail.com")
    context.login_page.enter_password("1234")


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    account_page = AccountPage(context.driver)
    assert account_page.display_account_information(), "Account information is not displayed"


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "Sameer" + time_stamp + "@gmail.com"
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("1234")


@then(u'I should get an error message')
def step_impl(context):
    error_message = "Warning: No match for E-Mail Address and/or Password."
    actual_value = context.login_page.warning_message_is_displayed()
    assert actual_value == error_message


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "Sameer" + time_stamp + "@gmail.com"
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("123456789")


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("fakeemail@gmail.com")
    context.login_page.enter_password("1234567")


@when(u'I do not enter anything in email address and password fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

