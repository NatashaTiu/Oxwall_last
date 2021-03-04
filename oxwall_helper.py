from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.internal_page import InternalPage
from pages.internal_pages.join_page import JoinPage
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage


class OxwallHelper:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_page = DashboardPage(driver)
        self.main_page = MainPage(driver)
        self.join_page = JoinPage(driver)
        self.login_page = LoginWindowPage(driver)
        self.internal_page = InternalPage(driver)

