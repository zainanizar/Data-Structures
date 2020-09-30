# Selection Sort


# O(n^2) time | O(1) space
def selectionSort(arr):

    for currentIdx in range(len(arr)):
        smallestIdx = currentIdx
        for i in range(smallestIdx, len(arr)):
            if arr[i] < arr[smallestIdx]:
                smallestIdx = i

        arr[currentIdx], arr[smallestIdx] = arr[smallestIdx], arr[currentIdx]

    return arr


arr = [8, 5, 2, 9, 5, 6, 3, 4, 9]
print(selectionSort(arr))
