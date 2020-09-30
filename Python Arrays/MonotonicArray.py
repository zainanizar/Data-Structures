# Monotic Arrays
# Determine whether the given array is monotic i.e.
# Monotic - entirely non-increasing or entirely non-decreasing


# O(n) time | O(1) space
def isMonotonic(arr):
    if len(arr) <= 2:
        return True

    def breakDirection(direction, prev, curr):
        diff = curr-prev
        # checking if increasing
        if direction > 0:
            return diff < 0
        # if decreasing
        return diff > 0

    direction = arr[1]-arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i]-arr[i-1]
            continue

        if breakDirection(direction, arr[i-1], arr[i]):
            return False

    return True


# O(n) time | O(1) space
def isMonotonic2(arr):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(arr)):
        curr = arr[i]
        prev = arr[i-1]

        if curr > prev:
            isNonIncreasing = False
        if curr < prev:
            isNonDecreasing = False

    return isNonDecreasing or isNonIncreasing


arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic2(arr))
