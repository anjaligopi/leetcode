import pytest

def func(x):
    return x + 5

def test_method():
    assert func(3) == 8
    assert func(3) == 11
    
if __name__ == "__main__":
    test_method()