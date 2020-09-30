# Insertion Sort


# O(n^2) time | O(1) space
def insertionSort(arr):

    for i in range(1, len(arr)):

        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr


arr = [2, 5, 4, 3, 7, 9, 1, 3, 4, 6]
print(insertionSort(arr))
