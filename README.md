## Как тестируем

Три подхода к организации тестов:

### 1. Skip Approach (`test_skip_approach.py`)

Общая фикстура `all_sizes` прогоняет тест на всех 6 разрешениях (3 десктопных + 3 мобильных). Внутри теста проверяется ширина экрана:
- Если разрешение не подходит для десктопа — тест пропускается через `pytest.skip()`
- Если разрешение не подходит для мобилки — тест пропускается через `pytest.skip()`

### 2. Indirect Approach (`test_indirect_approach.py`)

Фикстура `device` через `indirect=True` получает параметр ("desktop" или "mobile"). Page Object `GithubMainPage.click_sign_in()` использует нужный локатор.

### 3. Different Fixtures Approach (`test_fixture_approach.py`)

Две отдельные фикстуры: `desktop_button` и `mobile_button`. Каждая возвращает тип устройства. Тесты используют Page Object для клика.