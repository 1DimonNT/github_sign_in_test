import pytest
from selene import browser, be
from helpers.locators import DESKTOP_SIGN_IN, MOBILE_SIGN_IN


def test_desktop_skip(desktop_sizes):
    """Десктопный тест с пропуском мобильного разрешения"""
    browser.open("/")
    browser.element(DESKTOP_SIGN_IN).should(be.visible).click()
    print("✅ Desktop Sign In clicked")


def test_mobile_skip(mobile_sizes):
    """Мобильный тест с пропуском десктопного разрешения"""
    browser.open("/")
    browser.element(MOBILE_SIGN_IN).should(be.visible).click()
    print("✅ Mobile Sign In clicked")