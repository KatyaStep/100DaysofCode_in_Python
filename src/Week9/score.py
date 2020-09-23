def breakingRecords(scores):
    highest_score = 0
    lowest_score = 0
    low_count = 0
    high_count = 0

    for i in range(len(scores)):
        if i == 0:
            highest_score = scores[i]
            lowest_score = scores[i]
            continue
        if scores[i] < lowest_score:
            lowest_score = scores[i]
            low_count += 1
        if scores[i] > highest_score:
            highest_score = scores[i]
            high_count += 1

    return high_count, low_count


print(breakingRecords([0, 9, 3, 10, 2, 20]))
#a = [10, 5, 20, 20, 4, 5, 2, 25, 1]
#a = [17, 45, 41, 60, 17, 41, 76, 43, 51, 40, 89, 92, 34, 6, 64, 7, 37, 81, 32, 50]
#print(breakingRecords(a))