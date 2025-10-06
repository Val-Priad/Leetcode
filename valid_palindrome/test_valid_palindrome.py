import pytest
from main import valid_palindrome


@pytest.mark.parametrize(
    "msg, expected",
    [
        ("Was it a car or a cat I saw?", True),
        ("civic", True),
        ("deed", True),
        ("esse", True),
        ("kayak", True),
        ("keek", True),
        ("", True),
        (" ", True),
        ("a", True),
        ("A man, a plan, a canal: Panama", True),
        (".,", True),
    ],
)
def test_valid_palindrome_valid(msg: str, expected: bool):
    assert valid_palindrome(msg) == expected


@pytest.mark.parametrize(
    "msg, expected",
    [
        ("race a car", False),
        ("0P", False),
    ],
)
def test_valid_palindrome_invalid(msg: str, expected: bool):
    assert valid_palindrome(msg) == expected
