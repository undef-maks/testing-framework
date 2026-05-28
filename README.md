# Playwright POM Automation Framework

Цей фреймворк призначений для автоматизації UI та API тестування з використанням Python, Playwright, Pytest та патерну Page Object Model (POM).

---

## Структура проекту

- config/ — конфігурація проекту, базові налаштування та змінні для різних середовищ.
- pages/ — класи сторінок (Page Objects). base_page.py містить базові обгортки над методами Playwright.
- tests/ — набір тестів, розділений по рівнях, а також глобальні фікстури (conftest.py).
- utils/ — допоміжні утиліти (кастомний логер, хелпери для валідації даних тощо).

---

## Налаштування та запуск

1. Створіть та активуйте віртуальне оточення:
   python -m venv .venv
   source .venv/bin/activate.fish

2. Встановіть залежності та бінарники браузерів Playwright:
   pip install -r requirements.txt
   playwright install

3. Налаштуйте змінні оточення у файлі config/environments/dev.env (наприклад, BASE_URL, BROWSER, HEADLESS).

---

## Запуск тестів

Фреймворк розділений на три типи тестів залежно від рівня перевірки:

1. Unit-тести (перевірка утилітарних функцій та хелперів):
   env PYTHONPATH=. pytest tests/unit/ -v

2. Інтеграційні тести (тестування API через requests та Playwright APIRequestContext):
   env PYTHONPATH=. pytest tests/integration/ -v

3. UI-тести (автоматизація користувацького інтерфейсу через Playwright POM):
   env PYTHONPATH=. pytest tests/ui/ -v

4. **Системні тести** (End-to-End сценарії, логін та навігація):
   env PYTHONPATH=. pytest tests/system/ -v

_Щоб запустити взагалі всі тести одночасно, виконайте:_
env PYTHONPATH=. pytest -v
