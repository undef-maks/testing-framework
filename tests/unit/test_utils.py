import pytest
from utils.helpers import clean_text, is_valid_email, format_price

# --- Тести для clean_text ---
def test_clean_text_spaces():
    assert clean_text("  Привіт    Світ!  ") == "Привіт Світ!"

def test_clean_text_no_changes():
    assert clean_text("Нормальний рядок") == "Нормальний рядок"

def test_clean_text_wrong_type():
    with pytest.raises(TypeError):
        clean_text(123)


# --- Тести для is_valid_email ---
@pytest.mark.parametrize("email, expected", [
    ("user@example.com", True),
    ("user.name+tag@domain.co.uk", True),
    ("plainaddress", False),
    ("@missinguser.com", False),
    ("user@.com", False),
    (None, False)
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected


# --- Тести для format_price ---
def test_format_price_standard():
    assert format_price(1000) == "$1,000.00"
    assert format_price(10.5, currency="€") == "€10.50"

def test_format_price_float():
    assert format_price(1234567.891) == "$1,234,567.89"

def test_format_price_invalid_type():
    with pytest.raises(TypeError):
        format_price("тисяча")
