import os.path
import time

from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage
from pages.locators import DashboardPageLocators
from value_objects.user import User
from conftest import PROJECT_PATH


def test_create_user(driver, app, user):
    app.main_page.open_sign_up_page()
    app.join_page.input_username(user.username)
    app.join_page.input_email(user.email)
    app.join_page.input_password(user.password)
    app.join_page.repeat_password(user.password)
    app.join_page.input_real_name(user.real_name)
    if user.gender is not None:
        app.join_page.select_gender(user.gender)
    app.join_page.select_birthday(year=str(user.birthday[0]), month=user.birthday[1], day=user.birthday[2])
    app.join_page.select_looking_for(user.looking_for)
    app.join_page.select_here_for(user.here_for)
    app.join_page.input_music_text(user.music)
    app.join_page.input_favourite_books(user.favourite_books)
    app.join_page.upload_user_photo(os.path.join(PROJECT_PATH, 'data/photo.jpg'))
    app.join_page.press_join_button()
    assert app.dashboard_page.is_this_page() == True


def test_is_dashboard_page(driver, app, logged_user):
    app.internal_page.click_dashboard_link()
    time.sleep(3)
    driver.find_element(*DashboardPageLocators.TITLE_MY_DASHBOARD)
    assert app.dashboard_page.is_this_page() == True


def test_check_name_logged_in_user(driver, logged_user):
    user = User(username='admin', password='pass', real_name="Admin")
    dashboard_page = DashboardPage(driver)
    name = dashboard_page.user_icon.text
    assert name == user.real_name
    assert dashboard_page.active_menu.text == "MAIN"
    # assert dashboard_page.title.text == 'My Dashboard'


def test_login_positive(driver, user):
    # user = User(username='admin', password='pass', real_name="Admin")
    main_page = MainPage(driver)
    main_page.open_login_form()
    login_page = LoginWindowPage(driver)
    login_page.enter_credentials(user.username, user.password)
    assert login_page.wait_authentication()
    assert main_page.is_this_main_page()
    main_page.log_out()


