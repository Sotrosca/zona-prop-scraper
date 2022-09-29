import pytest
from src.browser import Browser


@pytest.fixture
def browser():
    return Browser()


class TestBrowser():
    def test_browser(self, browser):
        assert browser.get_text('https://www.google.com') is not None
