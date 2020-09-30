# Bubble Sort


# O(n^2) time | O(1) space
def bubbleSort(arr):

    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr)-1-counter):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False
        counter += 1

    return arr


# O(n^2) time | O(1) space
def bubbleSort2(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = [3, 4, 5, 1, 2, 6, 7, 2, 3, 4]
print(bubbleSort2(arr))
