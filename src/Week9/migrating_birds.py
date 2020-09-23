import collections

def migratoryBirds(arr):
    list_of_birds = collections.Counter(arr)
    migrating_birds_id = []
    max_birds = max(list_of_birds.values())
    for key, value in list_of_birds.items():
        if value == max_birds:
            migrating_birds_id.append(key)

    return min(migrating_birds_id)


print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
