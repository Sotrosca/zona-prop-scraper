import re
import time
from functools import reduce

from bs4 import BeautifulSoup

PAGE_URL_SUFFIX = '-pagina-'
HTML_EXTENSION = '.html'

FEATURE_UNIT_DICT = {
    'm²': 'square_meters_area',
    'amb': 'rooms',
    'dorm': 'bedrooms',
    'baño': 'bathrooms',
    'baños': 'bathrooms',
    'coch' : 'parking',
    }

LABEL_DICT = {
    'POSTING_CARD_PRICE' : 'price',
    'expensas' : 'expenses',
    'POSTING_CARD_LOCATION' : 'location',
    'POSTING_CARD_DESCRIPTION' : 'description',
}

class Scrapper:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def scrap_page(self, page_number):
        if page_number == 1:
            page_url = f'{self.base_url}{HTML_EXTENSION}'
        else:
            page_url = f'{self.base_url}{PAGE_URL_SUFFIX}{page_number}{HTML_EXTENSION}'

        print(f'URL: {page_url}')

        page = self.browser.get_text(page_url)

        soup = BeautifulSoup(page, 'lxml')
        estate_posts = soup.find_all('div', attrs = {'data-posting-type' : True})
        estates = []
        for estate_post in estate_posts:
            estate = self.parse_estate(estate_post)
            estates.append(estate)
        return estates

    def scrap_website(self):
        page_number = 1
        estates = []
        estates_scrapped = 0
        estates_quantity = self.get_estates_quantity()
        while estates_quantity > estates_scrapped:
            print(f'Page: {page_number}')
            estates += self.scrap_page(page_number)
            page_number += 1
            estates_scrapped = len(estates)
            time.sleep(3)

        return estates


    def get_estates_quantity(self):
        page_url = f'{self.base_url}{HTML_EXTENSION}'
        page = self.browser.get_text(page_url)
        soup = BeautifulSoup(page, 'lxml')
        soup.find_all('h1')[0].text

        estates_quantity = re.findall(r'\d+\.?\d+', soup.find_all('h1')[0].text)[0]

        estates_quantity = estates_quantity.replace('.', '')

        estates_quantity = int(estates_quantity)
        return estates_quantity

    def parse_estate(self, estate_post):
        # find div with anything data-qa atributte
        data_qa = estate_post.find_all('div', attrs={'data-qa': True})
        url = estate_post.get_attribute_list('data-to-posting')[0]
        estate = {}
        estate['url'] = url
        for data in data_qa:
            label = data['data-qa']
            text = None
            if label in ['POSTING_CARD_PRICE', 'expensas']:
                currency_value, currency_type = self.parse_currency_value(data.get_text())
                estate[LABEL_DICT[label] + '_' + 'value'] = currency_value
                estate[LABEL_DICT[label] + '_' + 'type'] = currency_type
            elif label in ['POSTING_CARD_LOCATION', 'POSTING_CARD_DESCRIPTION']:
                text = self.parse_text(data.get_text())
                estate[LABEL_DICT[label]] = text
            elif label in ['POSTING_CARD_FEATURES']:
                features = self.parse_features(data.get_text())
                estate.update(features)
            else:
                text = data.get_text()
                estate[label] = text
        return estate

    def parse_currency_value(self, text):
        try:
            currency_value = re.findall(r'\d+\.?\d+', text)[0]
            currency_value = currency_value.replace('.', '')
            currency_value = int(currency_value)
            currency_type = re.findall(r'(USD)|(ARS)|(\$)', text)[0]
            currency_type = [x for x in currency_type if x != ''][0]
            return currency_value, currency_type
        except:
            return text, None

    def parse_text(self, text):
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        text = text.strip()
        return text

    def parse_features(self, text):

        features_matches = re.compile(r'(\d+\.?\d*)\s(\w+)').findall(text)

        features_appearance = {'square_meters_area': 0, 'rooms': 0, 'bedrooms': 0, 'bathrooms': 0, 'parking' : 0}

        features = {}

        for feature in features_matches:
            try:
                feature_unit = f'{FEATURE_UNIT_DICT[feature[1]]}_{features_appearance[FEATURE_UNIT_DICT[feature[1]]]}'
                features_appearance[FEATURE_UNIT_DICT[feature[1]]] += 1
            except:
                feature_unit = feature[1]
            features[feature_unit] = feature[0]
        return features
