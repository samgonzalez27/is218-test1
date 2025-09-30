
from src.operations import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5


def test_subtract():
	assert subtract(5, 3) == 2


def test_multiply():
	assert multiply(4, 3) == 12


def test_divide():
	assert divide(10, 2) == 5
	assert divide(9, 3) == 3
	# Division by zero should raise
	import pytest
	with pytest.raises(ZeroDivisionError):
		divide(1, 0)
