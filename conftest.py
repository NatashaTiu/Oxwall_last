import os.path
import json
from datetime import date

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from db.db_connector import OxwallDB
from oxwall_helper import OxwallHelper
from pages.internal_pages.login_page import LoginWindowPage
from pages.internal_pages.main_page import MainPage
from value_objects.user import User

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_PATH)


@pytest.fixture(scope="session")
def config():
    with open(os.path.join(PROJECT_PATH, "config.json")) as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium):
    base_url = config["base_url"]
    dr = selenium
    dr.maximize_window()
    dr.implicitly_wait(5)
    dr.get(base_url)
    return dr


@pytest.fixture()
def app(driver):
    app = OxwallHelper(driver)
    return app


@pytest.fixture()
def logged_user(driver):
    user = User(username='admin', password='pass', real_name="Admin")
    main_page = MainPage(driver)
    main_page.open_login_form()
    login_page = LoginWindowPage(driver)
    login_page.enter_credentials(user.username, user.password)
    yield user
    main_page.log_out()


@pytest.fixture()
def db(config):
    db = OxwallDB(**config['db'])
    yield db
    db.close()


filename = os.path.join(PROJECT_PATH, 'data/user.json')
with open(filename, 'r', encoding='utf-8') as f1:
    user_list = json.load(f1)


@pytest.fixture(params=user_list, ids=[str(user) for user in user_list])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)








# User(username='Nata1', password='123qwe123', real_name="Natalia", email='dfgdfg@i.ua', gender=2,
#                 birthday=date(1985, 4, 6),  looking_for=[1, 2], here_for=[3, 4], music='Brainstorm, LP and others',
#                 fav_books='bla-bla-bla', is_admin=False)