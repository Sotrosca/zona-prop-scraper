from src.browser import Browser


# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    browser = Browser()
    assert func(3) == 4
