NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names():
    """Should return a list of title cased names,
       each name appears only once"""
    res = []
    [res.append(name.title()) for name in NAMES if name.title() not in res]

    return res


def sort_by_surname_desc():
    """Returns names list sorted desc by surname"""
    name = dedup_and_title_case_names()
    name.sort(key=lambda x: x.split()[1], reverse=True)

    return name


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    res = (min(names, key=len)).split()[0]

    return res

sort_by_surname_desc()