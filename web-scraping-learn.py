from bs4 import BeautifulSoup
import mechanize
import utils
import time
import pandas as pd
import numpy as np
from datetime import datetime
import re
from functools import reduce
import os

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

estates = []

url = 'https://www.zonaprop.com.ar/departamentos-alquiler-caseros-tres-de-febrero-villa-bosch-ciudad-jardin-lomas-del-palomar-martin-coronado-orden-publicado-descendente'

now = datetime.now().strftime("%d-%m-%Y_%H%M%S")

file_name = 'data-' + str(now)

csv_name = file_name + '.csv'
excel_name = file_name + '.xls'

there_are_more_estates = True
i = 1

estates_quantity = 0

estates_scrapped = 0

while there_are_more_estates:
    print("Page: " + str(i))
    if i == 1:
        page_url = url + '.html'
        page = browser.open(page_url).read()
    else:
        page_url = url + '-pagina-' + str(i) + '.html'
        page = browser.open(page_url).read()

    print("Page Retrieved")

    soup = BeautifulSoup(page, 'lxml')

    list_result_title = soup.find_all('h1', class_ = 'list-result-title')[0].text
    estates_quantity = int(reduce(lambda a, b : a + b ,re.findall(r'\d+', list_result_title)))

    registers = soup.find_all('div', class_ = 'postingCardInfo')

    print("Registers retrieved !!")

    for j, register in enumerate(registers):
        estate = utils.parse_estate(register)

        estates.append(estate)

        estates_scrapped += 1

    print('Estates parsed !!')
    print('Waiting ...')
    time.sleep(0.3)
    print('Continue')

    there_are_more_estates = estates_quantity > estates_scrapped

    i += 1

print('Scrapping finished !!!')
print(str(estates_scrapped) + ' estates scrapped.' )

dataframe = pd.DataFrame(estates)

relative_data_path = './data/'

if not os.path.exists(relative_data_path):
    os.mkdir(relative_data_path)

dataframe.to_csv(relative_data_path + csv_name, index=False)
dataframe.to_excel(relative_data_path + excel_name, index=False)

print('Data saved on ' + csv_name)
print('Excel saved on ' + excel_name)