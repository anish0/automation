from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_id = "input-email"
    password_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email_text):
        self.driver.find_element(By.ID, self.email_address_id).send_keys(email_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_id).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def warning_message_is_displayed(self):
        value = self.driver.find_element(By.XPATH, self.warning_message_xpath).text
        return value
