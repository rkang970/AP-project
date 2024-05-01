import random

letters = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
    "a": 27,
    "b": 28,
    "c": 29,
    "d": 30,
    "e": 31,
    "f": 32,
    "g": 33,
    "h": 34,
    "i": 35,
    "j": 36,
    "k": 37,
    "l": 38,
    "m": 39,
    "n": 40,
    "o": 41,
    "p": 42,
    "q": 43,
    "r": 44,
    "s": 45,
    "t": 46,
    "u": 47,
    "v": 48,
    "w": 49,
    "x": 50,
    "y": 51,
    "z": 52,
    "!": 53,
    "@": 54,
    "#": 55,
    "$": 56,
    "%": 57,
    "&": 58,
    "*": 59,
    "(": 60,
    ")": 61,
    "_": 62,
    "+": 63,
    "-": 64,
    "=": 65,
    "{": 66,
    "}": 67,
    "[": 68,
    "]": 69,
    "|": 70,
    ";": 71,
    ":": 72,
    "'": 73,
    '"': 74,
    ",": 75,
    ".": 76,
    "/": 77,
    "?": 78,
    "<": 79,
    ">": 80,
    "\\": 81,
    "`": 82,
    "~": 83,
    " ": 84,
    "0": 85,
    "1": 86,
    "2": 87,
    "3": 88,
    "4": 89,
    "5": 90,
    "6": 91,
    "7": 92,
    "8": 93,
    "9": 94
}

inverseLetters = {
    v:k for k,v in letters.items()
}

def generateKey(plaintext):
    
    key = random.choices(list(letters.keys()), k = len(plaintext))

    return "".join(key)

def encrypt():
    plaintext = input("Enter plaintext.")
    userInput = input("Would you like a random key? y/n")

    while userInput != "y" and userInput != "n":
        userInput = input("Answer must be 'y' or 'n'.")
    if userInput == "y":
        key = generateKey(plaintext)
    else:
        key = input("Enter key.")
    
    print("Your key is:", key)
    return xor(plaintext, key)

def decrypt():

    newText = ""

    ciphertext = input("Enter ciphertext.")
    ciphertext = ciphertext.split("|")
    key = input("Enter key.")

    for i in range(len(ciphertext)):

        keyidx = i % len(key)

        currentKey = letters[key[keyidx]]
        currentCiphertext = ciphertext[i]

        currentPlaintext = int(currentCiphertext) ^ currentKey
        newText += inverseLetters[currentPlaintext]
        
    return newText

    
def xor(plaintext, key):
    newText = ""

    for i in range(len(plaintext)):

        keyidx = i % len(key)
        currentPlaintext = letters[plaintext[i]] 
        currentKey = letters[key[keyidx]] 
        currentCiphertext = currentPlaintext ^ currentKey
        newText += str(currentCiphertext)

        if i != len(plaintext) - 1:
            newText += "|"

    return newText
    

if __name__ == "__main__":
    userInput = input("Would you like to encrypt or decrypt? (e/d)")

    while userInput != "e" and userInput != "d":
        userInput = input("Answer must be 'e' or 'd'.")

    if userInput == "e":
        print(encrypt())
        
    else:
        print(decrypt())