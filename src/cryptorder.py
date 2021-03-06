import os
import sys
import random
import string

os.system('cls' if os.name == 'nt' else 'clear')

characters = list(string.printable)

def encrypt(file, offset):
    chars = list(file)
    encrypted = []
    for char in chars:
        index = characters.index(char)
        if (index +  offset) > len(characters):
            difference = len(characters) - index
            remainder = index - difference
            index = remainder
        newChar = characters[index + offset]
        encrypted.append(newChar)
    return encrypted
        

path = input('Please specify file to encrypt: ')
offset = int(input('Please set the seed: '))
file = open(path, 'r')
print(encrypt(file.read(), offset))