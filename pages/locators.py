from selenium.webdriver.common.by import By


class InternalPageLocators:
    SIGN_IN = (By.XPATH, '//span[@class="ow_signin_label"]')
    BANNER_SUCCESSFUL_AUTHORIZATION = (By.XPATH, '//a [@class="close_button"]')
    USER_ICON = (By.XPATH, '//div [@class="ow_console_item ow_console_dropdown ow_console_dropdown_hover"]')
    USER_NAME = (By.XPATH, '//a [@class="ow_console_item_link"]')
    SIGN_OUT = (By.XPATH, '//li/div/a')
    SIGN_UP = (By.CLASS_NAME, 'ow_console_item_link')

    DASHBOARD = (By.XPATH, '//a/span[contains(text(), "Dashboard")]')
    ACTIVE_MENU = (By.CSS_SELECTOR, '.ow_responsive_menu .ow_main_menu .active')


class LoginPageLocators:
    USERNAME = (By.XPATH, '//input [@name="identity"]')
    PASSWORD = (By.XPATH, '//input [@name="password"]')
    SIGN_IN_BTN = (By.XPATH, '//input [@value="Sign In"]')


class MainPageLocators:
    NEEWSFEED_TITLE = (By.XPATH, '//h3 [@class="ow_ic_clock"]')


class DashboardPageLocators:
    TITLE_MY_DASHBOARD = (By.XPATH, '//h1 [@class="ow_stdmargin ow_ic_house"]')

    STATUS_FIELD = (By.XPATH, '//textarea [@name="status"]')
    ADD_PHOTO_FIELD = (By.XPATH, '//a [@class="image"]')
    SEND_BTN = (By.XPATH, '//input [@name="save"]')

    POST = (By.CSS_SELECTOR, 'div.ow_newsfeed_context_menu_wrap')
    CONTEXT_MENU = (By.XPATH, '//div [@class="ow_context_action"]')
    DELETE_BTN = (By.XPATH, '//a [@class="newsfeed_remove_btn owm_red_btn"]')

    POST_LIST = (By.XPATH, '//*[contains(@id, "action-feed1-")]')


class JoinPageLocators:
    USERNAME = (By.XPATH, '//input [@class="ow_username_validator"]')
    EMAIL = (By.XPATH, '//input [@class="ow_email_validator"]')
    PASSWORD = (By.XPATH, '//input [@name="password"]')
    REPEAT_PASSWORD = (By.XPATH, '//input [@name="repeatPassword"]')
    REAL_NAME = (By.XPATH, '//label[contains(text(), "Real name")]/../../td[2]/input')
    GENDER_RADIOBUTTON = (By.XPATH, '//label[contains(text(), "Gender")]/../../td[2]/ul/li[{}]/input')
    BIRTHDAY_DAY_DROPBOX = (By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[1]/select')
    BIRTHDAY_MONTH_DROPBOX = (By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[2]/select')
    BIRTHDAY_YEAR_DROPBOX = (By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[3]/select')
    LOOKING_FOR = (By.XPATH, '//label[contains(text(), "Looking for")]')
    HERE_FOR_CHECKBOX = (By.XPATH, '//label[text()="Here for"]')
    MUSIC_LISTBOX = (By.XPATH, '//label[text()="Music"]')
    BOOKS_LISTBOX = (By.XPATH, '//label[text()="Favorite books"]')
    USER_PHOTO = (By.XPATH, '//input[@name="userPhoto"]')
    APPLY_BUTTON = (By.XPATH, '//input[@id="avatar-crop-btn"]')
    JOIN_BUTTON = (By.XPATH, "//input[@name= 'joinSubmit'and@type='submit']")


class PostLocator:
    POST_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    LIKES_BUTTON = ()
    LIKES_COUNTER = ()
    COMMENTS_COUNTER = (By.CLASS_NAME, 'newsfeed_counter_comments')
    COMMENTS_BUTTON = ()



