from itertools import cycle
import random
import time

traffic_light = ['Red', 'Amber', 'Green']


def rand_timer():
    return random.randint(3, 7)


def traffic():
    colors = cycle(traffic_light)

    for color in colors:
        if color == 'Red':
            print(f'Stop! The light is {color}')
            time.sleep(rand_timer())
        elif color == 'Amber':
            print(f'Cautious! The light is {color}')
            time.sleep(rand_timer())
        else:
            print(f'Go! The light is {color}')
            time.sleep(rand_timer())


traffic()
