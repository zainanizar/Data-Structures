# Finding the three largest numbers in unsorted array


# O(n) time | O(1) space
def threeLargestNumbers(arr):
    threeLargest = [None, None, None]

    for num in arr:
        if threeLargest[2] is None or num > threeLargest[2]:
            shiftUpdate(threeLargest, num, 2)
        elif threeLargest[1] is None or num > threeLargest[1]:
            shiftUpdate(threeLargest, num, 1)
        elif threeLargest[0] is None or num > threeLargest[0]:
            shiftUpdate(threeLargest, num, 0)

    return threeLargest


def shiftUpdate(threeLargest, num, idx):
    for i in range(idx+1):
        if i == idx:
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i+1]


arr = [142, 1, 17, -7, -17, -27, 18, 540, 8, 7, 7]
print(threeLargestNumbers(arr))
