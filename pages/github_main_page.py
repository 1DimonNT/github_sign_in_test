from selene import browser, be
from helpers.locators import DESKTOP_SIGN_IN, MOBILE_SIGN_IN


class GithubMainPage:
    def open(self):
        browser.open("/")
        return self

    def click_sign_in(self, device_type: str):
        if device_type == "desktop":
            browser.element(DESKTOP_SIGN_IN).should(be.visible).click()
        else:
            browser.element(MOBILE_SIGN_IN).should(be.visible).click()
        return self