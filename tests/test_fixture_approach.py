import pytest
from selene import browser, be
from helpers.locators import DESKTOP_SIGN_IN, MOBILE_SIGN_IN


@pytest.fixture
def desktop_button():
    return DESKTOP_SIGN_IN


@pytest.fixture
def mobile_button():
    return MOBILE_SIGN_IN


def test_desktop_fixture(desktop_sizes, desktop_button):
    browser.open("/")
    browser.element(desktop_button).should(be.visible).click()
    print("✅ Desktop Sign In clicked")


def test_mobile_fixture(mobile_sizes, mobile_button):
    browser.open("/")
    browser.element(mobile_button).should(be.visible).click()
    print("✅ Mobile Sign In clicked")