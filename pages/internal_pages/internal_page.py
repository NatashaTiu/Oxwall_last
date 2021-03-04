from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
from pages.locators import InternalPageLocators


class InternalPage(Page):
    @property
    def sign_in_menu(self):
        return self.find_element(InternalPageLocators.SIGN_IN)

    @property
    def sign_out(self):
        return self.find_element(InternalPageLocators.SIGN_OUT)

    @property
    def sign_up(self):
        return self.find_element(InternalPageLocators.SIGN_UP)

    @property
    def user_icon(self):
        return self.find_visible_element(InternalPageLocators.USER_ICON)

    @property
    def active_menu(self):
        return self.find_element(InternalPageLocators.ACTIVE_MENU)

    def open_login_form(self):
        self.sign_in_menu.click()

    def open_sign_up_page(self):
        self.sign_up.click()

    def log_out(self):
        self.action.move_to_element(self.user_icon)
        self.action.pause(2)
        self.action.click(self.sign_out)
        self.action.perform()

    # def log_out(self):
    #     action1 = ActionChains(self.driver)
    #     hover = action1.move_to_element(user_icon)
    #     hover.perform()
    #
    #     action3 = ActionChains(self.driver)
    #     sign_out = action3.move_to_element(self.sign_out)
    #     sign_out.click(self.sign_out)
    #     sign_out.perform()

    def click_dashboard_link(self):
        dash = self.find_visible_from_many_equal(InternalPageLocators.DASHBOARD)
        dash.click()

    # def get_logged_in_user(self):
    #     return self.find_visible_from_many_equal(InternalPageLocators.USER_ICON)

