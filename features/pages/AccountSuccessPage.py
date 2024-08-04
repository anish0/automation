from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_created_xpath = "//div[@id='content']/h1"

    def account_created(self):
        actual_value = self.driver.find_element(By.XPATH, self.account_created_xpath).text
        return actual_value
