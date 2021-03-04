import json
import os.path
import pytest

from conftest import PROJECT_PATH
from data import random_string
from data.random_string import random_string2
from pages.internal_pages.dashboard_page import DashboardPage

file = os.path.join(PROJECT_PATH, 'data/post.json')
with open(file, 'r', encoding='utf-8') as f1:
    post_text_list = json.loads(f1.read())

# post_text_list = []
# post_text_list.append(random_string2(spaces=True))


@pytest.mark.parametrize('text', post_text_list)
def test_create_status(driver, logged_user, text):
    dashboard_page = DashboardPage(driver)
    counts_posts_before = len(dashboard_page.get_posts())
    dashboard_page.create_post(text=text, photo_path='/1.jpg')
    dashboard_page.wait_new_post_appear(counts_posts_before)
    posts = dashboard_page.get_posts()
    assert len(posts) == counts_posts_before + 1
    assert posts[0].text == text
    assert posts[0].user.real_name == logged_user.real_name and posts[0].user.username == logged_user.username
    assert posts[0].time == 'within 1 minute'
    dashboard_page.delete_post()





