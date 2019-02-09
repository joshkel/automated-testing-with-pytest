from fib import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5


def test_negative_fib():
    pass


def test_big_fib():
    assert fib(30) == 832040
