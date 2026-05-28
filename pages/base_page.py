from playwright.sync_api import Page
from utils.logger import logger
from config.config import settings

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = settings.TIMEOUT

    def open(self, url: str = ""):
        full_url = f"{settings.BASE_URL}{url}"
        logger.info(f"Відкриваємо сторінку: {full_url}")
        self.page.goto(full_url, timeout=self.timeout)

    def click(self, selector: str):
        logger.info(f"Клік на елемент: {selector}")
        self.page.wait_for_selector(selector, timeout=self.timeout)
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        logger.info(f"Введення тексту в {selector}")
        self.page.wait_for_selector(selector, timeout=self.timeout)
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.page.wait_for_selector(selector, timeout=self.timeout)
        return self.page.locator(selector).text_content()
