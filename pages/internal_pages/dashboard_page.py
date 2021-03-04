import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from pages.internal_pages.internal_page import InternalPage
from pages.locators import DashboardPageLocators
from custom_waits import presence_of_elements, elements_less_than_number
from pages.page_blocks.post_block import PostBlock


class DashboardPage(InternalPage):
    @property
    def status_field(self):
        return self.find_element(DashboardPageLocators.STATUS_FIELD)

    @property
    def photo_field(self):
        return self.find_clickable_element(DashboardPageLocators.ADD_PHOTO_FIELD)

    @property
    def save_btn(self):
        return self.find_element(DashboardPageLocators.SEND_BTN)

    @property
    def title(self):
        return self.find_visible_element(DashboardPageLocators.TITLE_MY_DASHBOARD)

    def get_posts(self):
        els = self.driver.find_elements(*DashboardPageLocators.POST_LIST)
        posts = [PostBlock(element) for element in els]
        return posts

    def create_post(self, text, photo_path):
        self.status_field.clear()
        self.status_field.send_keys(text)

        photo_field = self.wait.until(EC.element_to_be_clickable(DashboardPageLocators.ADD_PHOTO_FIELD))
        add_photo = self.driver.find_element(*DashboardPageLocators.ADD_PHOTO_FIELD).send_keys(photo_path)
        time.sleep(3)

        self.save_btn.click()
        # time.sleep(2)

    def wait_new_post_appear(self, number):
        return self.wait.until(presence_of_elements(DashboardPageLocators.POST_LIST, number+1))

    def delete_post(self):
        post = self.driver.find_elements(*DashboardPageLocators.POST)
        context_menu = self.driver.find_element(*DashboardPageLocators.CONTEXT_MENU)
        delete_btn = self.driver.find_element(*DashboardPageLocators.DELETE_BTN)

        action2 = self.action.move_to_element(post[0])
        action2.move_to_element(context_menu)
        action2.click(delete_btn)
        action2.perform()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()

    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD" and self.title.text == 'MY DASHBOARD'

        # try:
        #     self.driver.find_element(*DashboardPageLocators.TITLE_MY_DASHBOARD)
        # except NoSuchElementException:
        #     return False
        # else:
        #     return True