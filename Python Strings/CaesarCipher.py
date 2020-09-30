# Caesar Cipher Encryption


# O(n) time | O(n) space
def caesarCipher(string, key):

    cipher = []
    key = key % 26
    for char in string:
        asci = ord(char)
        if asci + key <= 122:
            cipherChar = chr(asci+key)
            cipher.append(cipherChar)
        else:
            cipherChar = chr(96+((asci+key) % 122))
            cipher.append(cipherChar)

    return "".join(cipher)


print(caesarCipher("wxyz", 4))
