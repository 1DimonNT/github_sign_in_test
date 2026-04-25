import pytest
from selene import browser, be
from helpers.locators import DESKTOP_SIGN_IN, MOBILE_SIGN_IN


@pytest.fixture
def sign_in_button(request):
    """Фикстура возвращает локатор в зависимости от типа теста"""
    if request.param == "desktop":
        return DESKTOP_SIGN_IN
    return MOBILE_SIGN_IN


@pytest.mark.parametrize("sign_in_button", ["desktop"], indirect=True)
def test_desktop_indirect(desktop_sizes, sign_in_button):
    browser.open("/")
    browser.element(sign_in_button).should(be.visible).click()
    print("✅ Desktop Sign In clicked")


@pytest.mark.parametrize("sign_in_button", ["mobile"], indirect=True)
def test_mobile_indirect(mobile_sizes, sign_in_button):
    browser.open("/")
    browser.element(sign_in_button).should(be.visible).click()
    print("✅ Mobile Sign In clicked")