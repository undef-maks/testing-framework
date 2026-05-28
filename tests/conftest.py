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
    # Захист від глобального $BROWSER з Linux
    valid_browsers = ["chromium", "firefox", "webkit"]
    browser_name = settings.BROWSER if settings.BROWSER in valid_browsers else "chromium"
    
    logger.info(f"Запуск браузера Playwright (конфіг/система: {settings.BROWSER} -> обрано рушій: {browser_name})")
    
    browser_type = getattr(playwright_instance, browser_name)
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

@pytest.fixture(scope="session")
def api_request_context(playwright_instance):
    logger.info("Ініціалізація Playwright APIRequestContext...")
    request_context = playwright_instance.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    logger.info("Закриття Playwright APIRequestContext.")
    request_context.dispose()
