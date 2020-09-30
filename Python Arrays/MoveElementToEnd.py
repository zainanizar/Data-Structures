# Move element to End
# Given an array move all the target numbers to the end of array


# O(n) time | O(1) space
def moveEleToEnd(arr, movEle):

    i = 0
    j = len(arr)-1
    while i < j:
        while i < j and arr[j] == movEle:
            j = j-1

        if arr[i] == movEle:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1

    return arr


arr = [2, 1, 2, 2, 3, 4, 2]
movEle = 2
print(moveEleToEnd(arr, movEle))
