from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
from pages.locators import LoginPageLocators, InternalPageLocators


class LoginWindowPage(Page):
    @property
    def username_field(self):
        return self.find_clickable_element(LoginPageLocators.USERNAME)

    @property
    def password_field(self):
        return self.find_clickable_element(LoginPageLocators.PASSWORD)

    @property
    def sign_in_btn(self):
        return self.find_clickable_element(LoginPageLocators.SIGN_IN_BTN)

    def enter_credentials(self, username, password):
        self.username_field.clear()
        self.username_field.send_keys(username)

        self.password_field.clear()
        self.password_field.send_keys(password)

        self.sign_in_btn.click()

    def wait_authentication(self):
        try:
            bunner_succesfull_authorization = self.wait.until(
            EC.presence_of_element_located(InternalPageLocators.BANNER_SUCCESSFUL_AUTHORIZATION),
            message='Bunner "Authentication success, please wait..." was not shown')
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea [@name="status"]')),
                   message='Locator Status_field not found ')
            return True
        except TimeoutException:
            return False

