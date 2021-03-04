import pytest


@pytest.mark.parametrize('text', ['Some text!', 'dfgsgdfgs dfsdfsf234234'])
def test_create_status(driver, oxwall, logged_user, text):
    oxwall.create_post(text=text, photo_path='D://study/infopulse/Oxwall_last/1.jpg')
    # assert





