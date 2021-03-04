from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.internal_pages.internal_page import InternalPage
from pages.locators import JoinPageLocators


class JoinPage(InternalPage):

    def input_username(self, text):
        name = self.find_visible_from_many_equal(JoinPageLocators.USERNAME)
        name.clear()
        name.send_keys(text)

    def input_email(self, text):
        email = self.find_visible_from_many_equal(JoinPageLocators.EMAIL)
        email.clear()
        email.send_keys(text)

    def input_password(self, password):
        pswd = self.find_visible_from_many_equal(JoinPageLocators.PASSWORD)
        pswd.clear()
        pswd.send_keys(password)

    def repeat_password(self, password):
        rep_pswd = self.find_visible_from_many_equal(JoinPageLocators.REPEAT_PASSWORD)
        rep_pswd.clear()
        rep_pswd.send_keys(password)

    def input_real_name(self, real_name):
        r_name = self.find_visible_from_many_equal(JoinPageLocators.REAL_NAME)
        r_name.clear()
        r_name.send_keys(real_name)

# gender=1 - male, 2-female
    def select_gender(self, gender):
        # GENDER_RADIOBUTTON = (By.XPATH, '//label[contains(text(), "Gender")]/../../td[2]/ul/li[{}]/input')
        locator = (JoinPageLocators.GENDER_RADIOBUTTON[0], JoinPageLocators.GENDER_RADIOBUTTON[1].format(gender))
        gender_field = self.find_visible_from_many_equal(locator)
        gender_field.click()

    def select_birthday(self, day, month, year):
        select_day = Select(self.find_visible_from_many_equal(JoinPageLocators.BIRTHDAY_DAY_DROPBOX))
        select_day.select_by_index(day)

        select_month = Select(self.find_visible_from_many_equal(JoinPageLocators.BIRTHDAY_MONTH_DROPBOX))
        select_month.select_by_index(month)

        select_year = Select(self.find_visible_from_many_equal(JoinPageLocators.BIRTHDAY_YEAR_DROPBOX))
        select_year.select_by_value(year)

    def select_looking_for(self, tuple1):
        label = self.find_visible_from_many_equal(JoinPageLocators.LOOKING_FOR)
        parent_node = label.find_element(By.XPATH, '../..')
        for i in tuple1:
            look_for = parent_node.find_element(By.XPATH, f'td[2]/ul/li[{i}]/input')
            look_for.click()

    def select_here_for(self, tuple1):
        here_for = self.find_visible_from_many_equal(JoinPageLocators.HERE_FOR_CHECKBOX)
        parent_node = here_for.find_element(By.XPATH, '../../td[2]/ul')
        for i in tuple1:
            here_for_checkbox = parent_node.find_element(By.XPATH, f'li[{i}]/input')
            here_for_checkbox.click()

    def input_music_text(self, text):
        label = self.find_visible_from_many_equal(JoinPageLocators.MUSIC_LISTBOX)
        parent_node = label.find_element(By.XPATH, '../..')
        music = parent_node.find_element(By.XPATH, 'td[2]/textarea')
        music.clear()
        music.send_keys(text)

    def input_favourite_books(self, books):
        label = self.find_visible_from_many_equal(JoinPageLocators.BOOKS_LISTBOX)
        parent_node = label.find_element(By.XPATH, '../..')
        book = parent_node.find_element(By.XPATH, 'td[2]/textarea')
        book.clear()
        book.send_keys(books)

    def upload_user_photo(self, file_path):
        photo_field = self.find_visible_from_many_equal(JoinPageLocators.USER_PHOTO)
        photo_field.send_keys(file_path)
        apply_btn = self.wait.until(EC.element_to_be_clickable(JoinPageLocators.APPLY_BUTTON))
        apply_btn.click()

    def press_join_button(self):
        join_btn = self.wait.until(EC.element_to_be_clickable(JoinPageLocators.JOIN_BUTTON))
        join_btn.click()






