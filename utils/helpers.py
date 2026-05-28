import re

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Вхідне значення має бути рядком")
    return " ".join(text.split())

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def format_price(amount: float, currency: str = "$") -> str:
    if not isinstance(amount, (int, float)):
        raise TypeError("Сума має бути числом")
    return f"{currency}{amount:,.2f}"

