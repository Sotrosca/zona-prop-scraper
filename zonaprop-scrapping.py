import datetime

import pandas as pd

from src.browser import Browser
from src.scrapper import Scrapper

if __name__ == '__main__':
    browser = Browser()
    base_url = 'https://www.zonaprop.com.ar/departamentos-alquiler'
    scrapper = Scrapper(browser, base_url)
    estates = scrapper.scrap_website()
    print('Scrapping finished !!!')
    df = pd.DataFrame(estates)
    filename = f'data/data-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv'
    df.to_csv(filename, index=False)
