# GitHub Sign In Tests

Три подхода к тестированию кнопки Sign In на GitHub.com с адаптацией под разные разрешения экрана.

## Подход 1: Skip Approach (test_github_skip_approach.py)

**Как работает:** В каждом тесте проверяется разрешение экрана. Если оно не подходит - тест пропускается через pytest.skip().

**Код:**
```python
def is_mobile_screen():
    return browser.config.window_width < 900

def test_desktop_sign_in_skip():
    if is_mobile_screen():
        pytest.skip("Только для десктопа")
    browser.open("/")
    browser.element("a.HeaderMenu-link--sign-in").click()

def test_mobile_sign_in_skip():
    if not is_mobile_screen():
        pytest.skip("Только для мобилки")
    browser.open("/")
    browser.element("a[href='/login']").click()
   ```
Плюсы: Простота, наглядность, легко читать.
Минусы: Логика дублируется в каждом тесте

Подход 2: Indirect Approach (test_github_indirect_approach.py)
Как работает: Фикстура возвращает локатор в зависимости от параметра. Параметр передается через indirect=True.
```python
@pytest.fixture
def sign_in_data(request):
    if request.param == "desktop":
        return "a.HeaderMenu-link--sign-in"
    return "a[href='/login']"

@pytest.mark.parametrize("sign_in_data", ["desktop"], indirect=True)
def test_desktop_indirect(sign_in_data):
    browser.open("/")
    browser.element(sign_in_data).click()

@pytest.mark.parametrize("sign_in_data", ["mobile"], indirect=True)
def test_mobile_indirect(sign_in_data):
    browser.open("/")
    browser.element(sign_in_data).click()
```
Плюсы: Централизованная логика, гибкость.
Минусы: Меньшая наглядность для новичков.

Подход 3: Different Fixtures Approach (test_github_fixture_approach.py)
Как работает: Создаются отдельные фикстуры для десктопа и мобилки. Тесты используют нужную фикстуру.
```python
@pytest.fixture
def desktop_setup():
    return "a.HeaderMenu-link--sign-in"

@pytest.fixture
def mobile_setup():
    return "a[href='/login']"

def test_desktop_fixture(desktop_setup):
    browser.open("/")
    browser.element(desktop_setup).click()

def test_mobile_fixture(mobile_setup):
    browser.open("/")
    browser.element(mobile_setup).click()
```
**Плюсы:** Максимальная читаемость, явное разделение.

**Минусы:** Больше кода.

---

## Сравнение

| Критерий | Skip | Indirect | Fixtures |
|----------|------|----------|----------|
| Простота | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Читаемость | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| DRY | ★★☆☆☆ | ★★★★☆ | ★★★★☆ |

---

## Запуск

```bash
pip install -r requirements.txt
```

# Десктоп

```bash
pytest -v --window-size=1920x1080
```

# Мобилка

```bash
pytest -v --window-size=375x667
```