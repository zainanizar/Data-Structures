# Longest Peak
# Find longest peak which has atleast three consecutive integers such if read
# from left to righ tthey are strictly increasing till peak and decreases strictly.


# O(n) time | O(1) space
def longestPeak(arr):

    longestPeakLength = 0
    i = 1
    while i < len(arr)-1:
        # finding peak
        isPeak = arr[i] > arr[i-1] and arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue

        # finding length of peak
        leftIdx = i-2
        while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx+1]:
            leftIdx -= 1
        rightIdx = i+2
        while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx-1]:
            rightIdx += 1

        currentPeakLength = rightIdx-leftIdx-1
        longestPeakLength = max(currentPeakLength, longestPeakLength)
        i = rightIdx

    return longestPeakLength


arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(arr))
