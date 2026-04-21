"""
Подход 2: Переопределение параметра через indirect=True
"""
import pytest
from selene import browser, be


DESKTOP_SIGN_IN_BUTTON = "a.HeaderMenu-link--sign-in"  # Исправленный локатор для десктопа
MOBILE_SIGN_IN_BUTTON = "a[href='/login']"  # Локатор для мобилки


@pytest.fixture
def sign_in_data(request) -> dict:
    """Фикстура возвращает данные для теста в зависимости от типа разрешения"""
    if request.param == "desktop":
        return {
            "locator": DESKTOP_SIGN_IN_BUTTON,
            "type": "desktop"
        }
    elif request.param == "mobile":
        return {
            "locator": MOBILE_SIGN_IN_BUTTON,
            "type": "mobile"
        }
    else:
        raise ValueError(f"Unknown test type: {request.param}")


def click_sign_in(locator: str):
    """Находит и нажимает кнопку Sign In"""
    browser.open("/")
    browser.element("body").should(be.visible)

    # Пробуем несколько локаторов если первый не сработал
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


@pytest.mark.parametrize("sign_in_data", ["desktop"], indirect=True)
def test_desktop_indirect(sign_in_data):
    """Десктопный тест с indirect параметризацией"""
    click_sign_in(sign_in_data["locator"])
    print(f"✅ Desktop test completed with type: {sign_in_data['type']}")


@pytest.mark.parametrize("sign_in_data", ["mobile"], indirect=True)
def test_mobile_indirect(sign_in_data):
    """Мобильный тест с indirect параметризацией"""
    click_sign_in(sign_in_data["locator"])
    print(f"✅ Mobile test completed with type: {sign_in_data['type']}")