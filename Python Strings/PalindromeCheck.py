# Determine whether given string is palindrome or not


# O(n^2) time | O(n) space  (Becoz of string memory allocation(static allocation))
def isPalindrome(string):
    reverse = ""
    for i in reversed(range(len(string))):
        reverse += string[i]

    return string == reverse


# O(n) time | O(n) space (Becoz of list memory allocation(dynamic allocation))
def isPalindrome2(string):
    reverseChars = []
    for i in reversed(range(len(string))):
        reverseChars.append(string[i])

    return string == "".join(reverseChars)


# O(n) time | O(n) space
def isPalindromeRecursive(string, i=0):
    j = len(string)-1-i

    return True if i >= j else string[i] == string[j] and isPalindromeRecursive(string, i+1)


# O(n) time | O(n) space
def isPalindromeRecursive2(string, i=0):
    j = len(string)-1-i

    if i >= j:
        return True
    elif string[i] != string[j]:
        return False
    else:
        return isPalindromeRecursive2(string, i+1)


# O(n) time | O(1) space
def isPalindromeOptim(string):
    leftIdx = 0
    rightIdx = len(string)-1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1

    return True


print(isPalindromeOptim("abcdcba"))
