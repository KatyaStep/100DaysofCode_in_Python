numbers_in_set = int(input())

while True:
    try:
        a_set = set(map(int, input().split()))
        if len(a_set) > numbers_in_set or len(a_set) < numbers_in_set:
            raise ValueError
        break
    except ValueError:
        print(f"Invalid set. The number of elements has to be {numbers_in_set}.")

number_other_sets = int(input())


for i in range(number_other_sets):
    command, length = input().split()
    other_set = set(map(int, input().split()))
    getattr(a_set, command)(other_set)

print(sum(a_set))
