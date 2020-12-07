import itertools

#
# names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
# locations = 'DE ES AUS NL BR US'.split()
# confirmed = ['False', 'True', 'True', 'False', 'True']
#
#
# def get_attendees():
#     for participant in itertools.zip_longest(names, locations, confirmed, fillvalue='-'):
#         print(participant)
#
#
# if __name__ == '__main__':
#     get_attendees()

friends = 'Bob Dante Julian Martin'.split()


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        func = itertools.permutations
    else:
        func = itertools.combinations
    return func(friends, team_size)

