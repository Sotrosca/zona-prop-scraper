import pytest
import pytest_mock
from src.scrapper import Scrapper


@pytest.fixture
def scrapper(mocker):
    browser = mocker.patch('src.scrapper.Browser')
    base_url = mocker.patch('src.scrapper.base_url')
    return Scrapper(browser, base_url)

class TestScrapper():
    def test_scrapper(self, scrapper):
        assert scrapper.scrap_website() is not None
