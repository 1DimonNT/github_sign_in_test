"""
Подход 1: Пропускаем тесты через pytest.skip()
"""
import pytest
from selene import browser, be


# Локаторы для кнопки Sign In
DESKTOP_SIGN_IN_BUTTON = "a[href='/login']"
MOBILE_SIGN_IN_BUTTON = "a[href='/login']"


def is_mobile_screen() -> bool:
    """Проверяем, что текущее разрешение - мобильное"""
    return browser.config.window_width < 900


def is_desktop_screen() -> bool:
    """Проверяем, что текущее разрешение - десктопное"""
    return browser.config.window_width >= 900


def click_sign_in_button():
    """Находит и нажимает кнопку Sign In"""
    browser.open("/")

    # Ждем загрузки страницы
    browser.element("body").should(be.visible)

    # Пробуем найти кнопку разными способами
    sign_in_selectors = [
        "a[href='/login']",
        "a.HeaderMenu-link--sign-in",
        "a[data-ga-click*='sign in']"
    ]

    for selector in sign_in_selectors:
        element = browser.element(selector)
        if element.with_(timeout=2).matching(be.visible):
            element.click()
            print(f"✅ Clicked using selector: {selector}")
            return

    # Если не нашли - ошибка
    raise Exception("Sign in button not found on the page")


def test_desktop_sign_in_skip():
    """Десктопный тест - пропускаем если мобильное разрешение"""
    if is_mobile_screen():
        pytest.skip("Этот тест только для десктопного разрешения (ширина >= 900px)")

    click_sign_in_button()
    print("✅ Desktop test completed successfully")


def test_mobile_sign_in_skip():
    """Мобильный тест - пропускаем если десктопное разрешение"""
    if is_desktop_screen():
        pytest.skip("Этот тест только для мобильного разрешения (ширина < 900px)")

    click_sign_in_button()
    print("✅ Mobile test completed successfully")