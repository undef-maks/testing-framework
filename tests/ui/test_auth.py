from utils.logger import logger

def test_failed_login(login_page):
    logger.info("Старт тесту: Невалідний логін")
    
    login_page.open("/login") 
    login_page.login("wrong_user", "wrong_password")
    
    error_text = login_page.get_error_text()
    assert "Invalid credentials" in error_text, f"Очікували помилку, але отримали: {error_text}"
    
    logger.info("Тест успішно завершено.")
