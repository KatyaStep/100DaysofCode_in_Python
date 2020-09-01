import os
import csv
from collections import defaultdict
import random
import pprint

data = dict()
side_dish = [
    'Brussel sprouts',
    'Carrots',
    'Cauliflower',
    'Corn',
    'Cornbread',
    'Fruit salad',
    'Green beans/green bean casserole',
    'Macaroni and cheese',
    'Mashed potatoes',
    'Rolls/biscuits',
    'Vegetable salad',
    'Yams/sweet potato casserole'
]
pies = [
    'Apple',
    'Buttermilk',
    'Cherry',
    'Chocolate',
    'Coconut cream',
    'Key lime',
    'Peach',
    'Pecan',
    'Pumpkin',
    'Sweet Potato'
]

deserts = [
    'Apple cobbler',
    'Blondies',
    'Brownies',
    'Carrot cake',
    'Cheesecake',
    'Cookies',
    'Fudge',
    'Ice cream',
    'Peach cobbler'
]


def read_data():
    folder = os.path.dirname(__file__)
    filename = os.path.join(folder, 'data', 'data.csv')

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        data.clear()
        for record in reader:
            region = record.get('US Region')
            income = record.get('How much total combined money did all members of your HOUSEHOLD earn last year?')

            if not region:
                continue

            if region not in data:
                data[ region ] = dict()
            if income not in data[ region ]:
                data[ region ][ income ] = set()

            for key, value in record.items():
                for side in side_dish:
                    if side in key and value.strip():
                        data[ region ][ income ].add(side)
                for pie in pies:
                    if pie in key and value.strip():
                        data[ region ][ income ].add(pie + ' pie')
                for desert in deserts:
                    if desert in key and value.strip():
                        data[ region ][ income ].add(desert)
        # pprint.pprint(data)
    return data


def app():
    question = input('Do you celebrate Thanksgiving?: ')
    if question.lower() == 'yes':
        records = read_data()
        # regions = "\n".join([str((index+1, record)).strip("()") for index, record in enumerate(records.keys())])
        #regions = "\n".join([f'{index + 1}. {record}' for index, record in enumerate(records.keys())])
        regions = defaultdict()
        income = defaultdict()
        for index, record in enumerate(records.keys()):
            regions[index+1] = record

        print('Choose your region: ')
        [print(key, value) for key, value in regions.items()]

        region_key = int(input('Enter a number: '))
        user_region = regions[region_key]
        # user_region = input('Enter: ')
        # number_region = input('Enter: ')
        # region_index = int(regions.find(number_region))
        # user_region = regions[region_index+2:].strip()
        # print(user_region)
        # income = "\n".join([f'{index+1}. {record}' for index, record in enumerate(records[user_region])])
        for index, record in enumerate(records[user_region]):
            income[index] = record

        print("Choose your income: ")
        [print(key, value) for key, value in income.items()]

        income_key = int(input('Enter a number of the income in the menu: '))
        user_income = income[income_key]
        # print(f"Choose your income:\n {income} ")
        # user_income = input('Enter: ')
        # print('---------------')
        food = list(records[user_region][user_income])
        print('\n'.join(random.choices(food, k=5)))
        return True
    else:
        print('Good Bye!')


#app()
