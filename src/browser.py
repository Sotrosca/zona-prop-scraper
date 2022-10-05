import cloudscraper


class Browser():
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def get(self, url):
        return self.scraper.get(url)

    def post(self, url, data):
        return self.scraper.post(url, data)

    def get_text(self, url):
        return self.scraper.get(url).text

