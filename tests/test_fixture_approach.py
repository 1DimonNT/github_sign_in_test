import pytest
from pages.github_main_page import GithubMainPage


@pytest.fixture
def desktop_button():
    return "desktop"


@pytest.fixture
def mobile_button():
    return "mobile"


def test_desktop_fixture(desktop_sizes, desktop_button):
    page = GithubMainPage()
    page.open().click_sign_in(desktop_button)
    print("✅ Desktop test with fixture approach")


def test_mobile_fixture(mobile_sizes, mobile_button):
    page = GithubMainPage()
    page.open().click_sign_in(mobile_button)
    print("✅ Mobile test with fixture approach")