import os
import csv
import random
import pprint
import collections

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
            # record = parse_row(record)
            # print('reg', record.get('US Region'))
            # print('inc', '\t',
            #       record.get('How much total combined money did all members of your HOUSEHOLD earn last year?'))
            # for key, value in record.items():
            #     if ('Which of these desserts do you typically have at Thanksgiving dinner?' in key and value.strip()):
            #         print('\t\t', value)
            # # print(record.get('US Region'))
            # data.append(record)
            # print(type(record))
            region = record.get('US Region')
            income = record.get('How much total combined money did all members of your HOUSEHOLD earn last year?')

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
    # question = input('Do you celebrate Thanksgiving? ')
    records = read_data()
    regions = "\n".join(list(records.keys()))
    print(f"Choose your US region from:\n {regions} ")
    user_region = input('Enter: ')
    income = "\n".join(list(records[user_region]))
    print(f"Choose your income:{income} ")
    user_income = input('Enter: ')
    print('---------------')
    #food = ",".join(list(records[ 'New England' ][ user_income ]))
    food = list(records[user_region][user_income])
    print('\n'.join(random.choices(food, k=5)))


app()
