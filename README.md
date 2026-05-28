# Playwright POM Automation Framework

Цей фреймворк призначений для автоматизації UI-тестування з використанням Python, Playwright, Pytest та патерну Page Object Model (POM).

## Структура проекту

- `config/` — конфігураційні файли для різних середовищ (.env).
- `pages/` — класи сторінок (Page Objects). `base_page.py` містить базові обгортки над методами Playwright.
- `tests/` — UI тести та конфігурація тестів (`conftest.py`).
- `utils/` — утиліти (логер тощо).

## Налаштування та запуск

1. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
