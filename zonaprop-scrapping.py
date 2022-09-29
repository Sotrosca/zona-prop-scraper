import json

import pandas as pd

from browser import Browser
from scrapper import Scrapper


def save_to_json(estates):
    with open('zonaprop.json', 'w') as f:
        json.dump(estates, f)


if __name__ == '__main__':
    browser = Browser()
    base_url = 'https://www.zonaprop.com.ar/departamentos-alquiler-caseros-tres-de-febrero-villa-bosch-ciudad-jardin-lomas-del-palomar-martin-coronado-orden-publicado-descendente'
    scrapper = Scrapper(browser, base_url)
    estates = scrapper.scrap_website()
    print('Scrapping finished !!!')
    save_to_json(estates)
    df = pd.DataFrame(estates)
    df.to_csv('zonaprop.csv', index=False)
