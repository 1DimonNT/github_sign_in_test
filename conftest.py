"""
Общие фикстуры и хуки для всех подходов
"""
import allure
import pytest
from selene import browser


def pytest_addoption(parser):
    """Добавляем кастомные опции командной строки"""
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests"
    )
    parser.addoption(
        "--window-size",
        default="1920x1080",
        help="Window size in format WIDTHxHEIGHT"
    )


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    """Настройка браузера для каждого теста"""
    # Получаем размер окна из параметров
    window_size = request.config.getoption("--window-size")
    width, height = map(int, window_size.split("x"))

    # Настройка браузера
    browser.config.base_url = "https://github.com"
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.timeout = 5.0

    # Логируем какой тест запускается с каким разрешением
    test_type = "mobile" if width < 900 else "desktop"
    print(f"\n🐛 Running test: {request.node.name}")
    print(f"📱 Screen size: {width}x{height} ({test_type})")

    yield

    # Закрываем браузер после теста
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Делаем скриншот при падении теста (опционально)"""
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        # Здесь можно добавить логику скриншота
        # screenshot = browser.driver.get_screenshot_as_png()
        # allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
        print(f"❌ Test failed: {item.name}")