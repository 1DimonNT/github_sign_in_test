"""
Подход 3: Разные фикстуры для каждого теста
"""
import pytest
from selene import browser, be


DESKTOP_SIGN_IN_BUTTON = "a.HeaderMenu-link--sign-in"  # Локатор для десктопа
MOBILE_SIGN_IN_BUTTON = "a[href='/login']"  # Локатор для мобилки


def click_sign_in(locator: str):
    """Общая логика нажатия на кнопку Sign In"""
    browser.open("/")
    browser.element("body").should(be.visible)

    # Пробуем несколько локаторов
    selectors_to_try = [
        locator,
        "a[href='/login']",
        "a.HeaderMenu-link--sign-in"
    ]

    for selector in selectors_to_try:
        element = browser.element(selector)
        if element.with_(timeout=2).matching(be.visible):
            element.click()
            print(f"✅ Clicked using selector: {selector}")
            return

    raise Exception(f"Sign in button not found with locator: {locator}")


@pytest.fixture
def desktop_setup():
    """Фикстура для десктопных тестов"""
    print("\n💻 Setting up desktop test")
    return DESKTOP_SIGN_IN_BUTTON


@pytest.fixture
def mobile_setup():
    """Фикстура для мобильных тестов"""
    print("\n📱 Setting up mobile test")
    return MOBILE_SIGN_IN_BUTTON


def test_desktop_fixture(desktop_setup):
    """Десктопный тест использует desktop_setup фикстуру"""
    click_sign_in(desktop_setup)
    print("✅ Desktop test completed")


def test_mobile_fixture(mobile_setup):
    """Мобильный тест использует mobile_setup фикстуру"""
    click_sign_in(mobile_setup)
    print("✅ Mobile test completed")