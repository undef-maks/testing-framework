import re

def clean_text(text: str) -> str:
    """Видаляє зайві пробіли на початку, в кінці та повторення всередині рядка."""
    if not isinstance(text, str):
        raise TypeError("Вхідне значення має бути рядком")
    return " ".join(text.split())

def is_valid_email(email: str) -> bool:
    """Перевіряє, чи відповідає рядок базовому формату email."""
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def format_price(amount: float, currency: str = "$") -> str:
    """Форматує число у грошовий вигляд (наприклад, 1250.5 -> $1,250.50)."""
    if not isinstance(amount, (int, float)):
        raise TypeError("Сума має бути числом")
    return f"{currency}{amount:,.2f}"
