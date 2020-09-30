# Binary Search


# O(Log(n)) time | O(Log(n)) Space
def binarySearch(arr, left, right, target):

    if left > right:
        return -1

    mid = (left+right)//2
    match = arr[mid]
    if target == match:
        return mid

    elif target > match:
        return binarySearch(arr, mid+1, right, target)

    elif target < match:
        return binarySearch(arr, left, mid-1, target)


# O(Log(n)) time | O(Log(n)) Space
def binarySearch2(arr, left, right, target):

    while left <= right:

        mid = (left+right)//2
        match = arr[mid]
        if target == match:
            return mid

        elif target > match:
            left = mid+1

        elif target < match:
            right = mid-1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
print(binarySearch(arr, 0, len(arr)-1, target))
