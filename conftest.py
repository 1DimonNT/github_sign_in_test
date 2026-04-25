import pytest
from selene import browser


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--window-size", default="1920x1080")


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    window_size = request.config.getoption("--window-size")
    width, height = map(int, window_size.split("x"))

    browser.config.base_url = "https://github.com"
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.timeout = 5.0

    print(f"\n=== Running: {request.node.name} ===")
    print(f"Screen: {width}x{height}")

    yield

    browser.quit()


# Фикстуры с разными разрешениями
@pytest.fixture(params=[(1920, 1080), (1366, 768), (1280, 720)])
def desktop_sizes(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    print(f"\n=== Desktop test: {width}x{height} ===")
    yield width
    browser.quit()


@pytest.fixture(params=[(375, 667), (414, 896), (360, 780)])
def mobile_sizes(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    print(f"\n=== Mobile test: {width}x{height} ===")
    yield width
    browser.quit()