import random

def generateKey():
    key = ""
    for i in range(6):
        key += str(random.randint(0,1))
    return int(key)

def encrypt():
    plaintext = input("Enter plaintext.")
    userInput = input("Would you like a random key? y/n")

    while userInput != "y" or userInput != "n":
        userInput = input("Answer must be 'y' or 'n'.")
    if userInput == "y":
        key = generateKey()
    else:
        key = input("Enter key.")

def xor():
    


    

    
# def encrypt(word: str, key: str) -> str:
#     word = plaintext
#     binaryValues = []
#     for i in range(len(word)):
#         binaryValues.append((int(bin(ord(word[i]))[2:])) ^ key)

#     return binaryValues


if __name__ == "__main__":
    userInput = input("Would you like to encrypt or decrypt? (e/d)")

    while userInput != "e" or userInput != "d":
        userInput = input("Answer must be 'e' or 'd'.")

    if userInput == "e":
        print(encrypt())
        
    else:
        cipherText = input("Enter phrase to be decrypted.")

