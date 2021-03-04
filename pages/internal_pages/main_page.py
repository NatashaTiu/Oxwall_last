from pages.internal_pages.internal_page import InternalPage
from pages.locators import MainPageLocators


class MainPage(InternalPage):
    def is_this_main_page(self):
        try:
            self.driver.find_element(*MainPageLocators.NEEWSFEED_TITLE)
        except Exception:
            return False
        else:
            return True

