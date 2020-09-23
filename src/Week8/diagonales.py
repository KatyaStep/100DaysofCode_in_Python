arr = [[1, 2, 3],
       [4,5,6],
       [8,8,9]
       ]

def diagonalDifference(arr):
    # Write your code here
    left_to_right = 0
    right_to_left = 0
    for row in arr:
        print(row, end='\n')

    col = 0
    row = len(arr) - 1

    # left to right
    for index in range(len(arr)):
        left_to_right += arr[index][col]
        col += 1

    # right to left
    for index in range(len(arr)):
        right_to_left += arr[index][row]
        row -= 1

    print(abs(left_to_right - right_to_left))



diagonalDifference(arr)