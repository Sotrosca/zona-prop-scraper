import pytest_mock
from src.scraper import Scraper


class TestScraper():

    def test_scraper(self, mocker: pytest_mock.MockFixture, html_page: str):
        browser = mocker.patch('src.browser.Browser')
        scraper = Scraper(browser, 'fake_url.com')
        scraper.get_estates_quantity = mocker.MagicMock(return_value=20)
        browser.get_text = mocker.MagicMock(return_value=html_page)
        estates = scraper.scrap_website()
        assert len(estates) == 20
