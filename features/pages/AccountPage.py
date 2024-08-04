from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    edit_account_information_xpath = "//a[normalize-space()='Edit your account information']"

    def display_account_information(self):

        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.edit_account_information_xpath))
        ).is_displayed()

