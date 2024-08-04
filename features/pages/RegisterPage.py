from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    privacy_policy_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_xpath = "//label[normalize-space()='Yes']"
    duplicate_account_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_warning_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    lastname_warning_xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_warning_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    password_warning_xpath = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephone_id).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(confirm_password)

    def click_privacy_policy(self):
        self.driver.find_element(By.NAME, self.privacy_policy_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def click_newsletter(self):
        self.driver.find_element(By.XPATH, self.newsletter_xpath).click()

    def display_duplicate_email_warning(self):
        actual_message = self.driver.find_element(By.XPATH, self.duplicate_account_warning_xpath).text
        return actual_message

    def display_status_of_all_warning(self, expected_privacy_warning, expected_fn_warning, expected_ln_warning,
                                      expected_email_warning, expected_password_warning):
        privacy_warning = (self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text.__contains__
                           (expected_privacy_warning))
        firstname_warning = ((self.driver.find_element(By.XPATH, self.firstname_warning_xpath)).text.__contains__
                             (expected_fn_warning))
        lastname_warning = ((self.driver.find_element(By.XPATH, self.lastname_warning_xpath)).text.__contains__
                            (expected_ln_warning))
        email_warning = ((self.driver.find_element(By.XPATH, self.email_warning_xpath)).text.__contains__
                         (expected_email_warning))
        password_warning = ((self.driver.find_element(By.XPATH, self.password_warning_xpath)).text.__contains__
                            (expected_password_warning))
        if privacy_warning and firstname_warning and lastname_warning and email_warning and password_warning:
            return True
        else:
            return False
