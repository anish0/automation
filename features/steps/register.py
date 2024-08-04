from behave import *
from selenium.webdriver.common.by import By
from datetime import datetime
from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I am in register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_register_option()
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@when(u'I enter mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("sameer")
    context.register_page.enter_last_name("khadka")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "Sameer" + time_stamp + "@gmail.com"
    context.register_page.enter_email(new_email)
    context.register_page.enter_telephone("212212111")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm_password("12345")


@When(u'I select privacy policy option')
def step_impl(context):
    context.register_page.click_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.click_continue_button()


@then(u'Account should get created')
def step_impl(context):
    expected_value = "Your Account Has Been Created!"
    context.account_success_page = AccountSuccessPage(context.driver)
    actual_value = context.account_success_page.account_created()
    assert expected_value == actual_value, f"Expected: '{expected_value}', but got: '{actual_value}'"


@when(u'I enter all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("sameer")
    context.register_page.enter_last_name("khadka")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "Sameer" + time_stamp + "@gmail.com"
    context.register_page.enter_email(new_email)
    context.register_page.enter_telephone("212212111")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm_password("12345")
    context.register_page.click_newsletter()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("sameer")
    context.register_page.enter_last_name("khadka")
    context.register_page.enter_telephone("212212111")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm_password("12345")
    context.register_page.click_newsletter()


@when(u'I enter existing email address into email field')
def step_impl(context):
    context.register_page.enter_email("sunil.timsina@creospan.com")


@then(u'A proper error message should be shown')
def step_impl(context):
    warning_message = "Warning: E-Mail Address is already registered!"
    actual_message = context.register_page.display_duplicate_email_warning()
    assert warning_message == actual_message


@when(u'I do not enter anything in the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password("")
    context.register_page.click_newsletter()


@then(u'A proper error message should be shown for mandatory fields')
def step_impl(context):
    expected_privacy = "Warning: You must agree to the Privacy Policy!"
    expected_firstname = "First Name must be between 1 and 32 characters!"
    expected_lastname = "Last Name must be between 1 and 32 characters!"
    expected_email = "E-Mail Address does not appear to be valid!"
    expected_password = "Password must be between 4 and 20 characters!"
    context.register_page.display_status_of_all_warning(expected_privacy, expected_firstname, expected_lastname,
                                                        expected_email, expected_password)
