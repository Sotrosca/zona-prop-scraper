import time

def parse_expenses(expenses_string):
    return int(expenses_string.replace('Expensas', '').replace('+ $', '').replace('.', ''))

def parse_badge_and_prize(badge_and_prize_string):
    return badge_and_prize_string.split(' ')

def parse_estate(register):
    estate = {}

    prize = register.find('span', class_='firstPrice')
    if prize:
        badge_and_prize_string = register.find('span', class_='firstPrice').text.strip()
        badge_and_prize = parse_badge_and_prize(badge_and_prize_string)
        if len(badge_and_prize) > 1:
            estate['badge'] = badge_and_prize[0]
            estate['prize'] = int(badge_and_prize[1].replace('.', ''))
        else:
            estate['prize'] = int(badge_and_prize[0].replace('.', ''))

    expenses = register.find('span', {"data-qa" : "expensas"})
    if expenses and estate.get('prize'):
        estate['expenses'] = parse_expenses(register.find('span', {"data-qa" : "expensas"}).text.strip().replace('\n', ''))
        estate['prize+expenses'] = estate.get('expenses') + estate.get('prize')
    else:
        estate['prize+expenses'] = estate.get('prize')

    address = register.find('span', {"data-qa" : "direccion"})
    if address:
        estate['address'] = register.find('span', {"data-qa" : "direccion"}).text.strip()

    location = register.find('span', {"data-qa" : "ubicacion"})
    if location:
        estate['location'] = register.find('span', {"data-qa" : "ubicacion"}).text.strip()

    features = register.find('ul', {"data-qa" : "features"})

    for feature_li in features.find_all('li'):
        feature_name = feature_li.find('i').get('class')[1][4:]
        feature_value = feature_li.text.strip().replace('\n', ' ')
        estate[feature_name] = feature_value.split(' ')[0]


    a_go_to_posting = register.find('a', class_='go-to-posting')

    estate['href'] = a_go_to_posting.get('href')
    estate['description'] = a_go_to_posting.text.strip()

    published_date = register.find('div', class_='publishedDate')

    estate['published-date'] = published_date.text.strip().replace('\n', ' ')

    return estate


