import pytest
import calc

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-2, -2) == 0

def test_multiply():
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-1, 5) == -5
    assert calc.multiply(0, 100) == 0

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_square_root():
    assert calc.square_root(9) == 3
    assert calc.square_root(0) == 0
    with pytest.raises(ValueError):
        calc.square_root(-4)

def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -2) == 0.25

def test_factorial():
    assert calc.factorial(0) == 1
    assert calc.factorial(1) == 1
    assert calc.factorial(5) == 120
    with pytest.raises(ValueError):
        calc.factorial(-3)