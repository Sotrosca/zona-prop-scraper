import pytest
import pytest_mock
from src.scrapper import Scrapper


class TestScrapper():

    def test_scrapper(self, mocker: pytest_mock.MockFixture, html_page: str):
        browser = mocker.patch('src.browser.Browser')
        scrapper = Scrapper(browser, 'fake_url.com')
        scrapper.get_estates_quantity = mocker.MagicMock(return_value=20)
        browser.get_text = mocker.MagicMock(return_value=html_page)
        estates = scrapper.scrap_website()
        assert len(estates) == 20
