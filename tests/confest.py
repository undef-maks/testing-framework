import pytest
from playwright.sync_api import sync_playwright
from config.config import settings
from utils.logger import logger
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def playwright_instance():
    logger.info("Ініціалізація Playwright...")
    with sync_playwright() as p:
        yield p
    logger.info("Закриття Playwright.")

@pytest.fixture(scope="session")
def browser(playwright_instance):
    logger.info(f"Запуск браузера: {settings.BROWSER}")
    browser_type = getattr(playwright_instance, settings.BROWSER)
    browser = browser_type.launch(headless=settings.HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    logger.info("Створення нового контексту та сторінки")
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)
