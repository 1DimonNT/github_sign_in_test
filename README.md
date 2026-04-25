# GitHub Sign In Tests

Автотесты кнопки Sign In на GitHub.com для десктопных и мобильных разрешений экрана.

## Что тестируем

Открываем главную страницу GitHub, находим кнопку "Sign in", нажимаем на неё.

## Как тестируем

Три подхода к организации тестов:

### 1. Skip Approach (`test_skip_approach.py`)

Фикстуры `desktop_sizes` и `mobile_sizes` сами прогоняют тест на всех разрешениях. Проверка внутри теста не нужна.

### 2. Indirect Approach (`test_indirect_approach.py`)

Фикстура `sign_in_button` через `indirect=True` получает параметр ("desktop" или "mobile") и возвращает нужный локатор.

### 3. Different Fixtures Approach (`test_fixture_approach.py`)

Две отдельные фикстуры: `desktop_button` и `mobile_button`. Каждый тест берёт свою.

## Какие разрешения

| Тип | Разрешения |
|-----|-------------|
| Десктоп | 1920x1080, 1366x768, 1280x720 |
| Мобильные | 375x667, 414x896, 360x780 |

## Запуск

```bash
pip install -r requirements.txt
pytest tests/ -v