import pytest

def func(x):
    return x + 5

# to test multiple test cases, use this mark decorator
@pytest.mark.test1
def test_method1():
    assert func(3) == 8

@pytest.mark.test2
def test_method2():
    assert func(3) == 11
    
# Run iusing pytest sample-pytest.py -m test1

# if __name__ == "__main__":
#     # test_method1()
#     # test_method2()
#     # func(8)
#     pass