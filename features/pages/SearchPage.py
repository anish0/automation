from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    searched_item_link_text = "HP LP3065"
    error_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def is_searched_item_displayed(self):
        try:
            element = self.driver.find_element(By.LINK_TEXT, self.searched_item_link_text)
            return element.is_displayed()
        except:
            return False

    def error_message(self):
        message = self.driver.find_element(By.XPATH, self.error_message_xpath).text
        return message
