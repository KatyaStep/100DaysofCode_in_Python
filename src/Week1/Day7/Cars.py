cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    model = 'Jeep'

    # if model in cars:
    #     for car in cars[model]:
    #         print(f"{car}", end=", ")
    #     return True
    # else:
    #     return print('There is no such model in car. Try again!')

    for car in cars.keys():
        if car == model:
            res = ", ".join(cars[car])
    return res


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = list()

    for car in cars.keys():
        first_model.append(cars[car][0])

    return first_model


def get_all_matching_models(cars=cars, grep='CO'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matching_cars = list()

    for models in cars.values():
        for model_name in models:
            if grep.lower() in model_name.lower():
                matching_cars.append(model_name)

    matching_cars.sort()
    return matching_cars


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_cars = dict()
    for car, models in cars.items():
        models.sort()
        sorted_cars[car] = models

    return sorted_cars


def main():
    get_all_jeeps()
    get_first_model_each_manufacturer()
    get_all_matching_models()
    sort_car_models()


if __name__ == '__main__':
    main()
