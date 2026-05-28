import pytest
from utils.logger import logger

def test_system_flow(login_page, page):
    logger.info("СТАРТ СИСТЕМНОГО ТЕСТУ: Повний цикл користувача")
    
    login_page.open("") 
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    logger.info("Перевірка переходу на системну сторінку...")
    # приклад
    assert page.url == "https://the-internet.herokuapp.com/secure"
