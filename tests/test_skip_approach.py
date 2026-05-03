import pytest
from selene import browser, be
from helpers.locators import DESKTOP_SIGN_IN, MOBILE_SIGN_IN


def is_mobile(width):
    return width < 900


def is_desktop(width):
    return width >= 900


def test_desktop_skip(all_sizes):
    """Десктопный тест - пропускаем мобильные разрешения"""
    width = all_sizes

    if is_mobile(width):
        pytest.skip(f"Desktop test skipped for mobile resolution {width}x…")

    browser.open("/")
    browser.element(DESKTOP_SIGN_IN).should(be.visible).click()
    print(f"✅ Desktop test passed on {width}x…")


def test_mobile_skip(all_sizes):
    """Мобильный тест - пропускаем десктопные разрешения"""
    width = all_sizes

    if is_desktop(width):
        pytest.skip(f"Mobile test skipped for desktop resolution {width}x…")

    browser.open("/")
    browser.element(MOBILE_SIGN_IN).should(be.visible).click()
    print(f"✅ Mobile test passed on {width}x…")