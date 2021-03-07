import os
import sys
import random
import string

os.system('cls' if os.name == 'nt' else 'clear')

characters = list(string.printable)

def readFile(path):
    file = open(path, 'r')
    lines = file.read().splitlines()
    chars = []
    for line in lines:
        splitLine = list(line)
        chars.append(splitLine)
    return chars

def stringify(chars):
    string = ''
    for char in chars:
        string += char
    return string

def output(lines, fileName, mode):
    extension = 'txt'
    if mode == True: extension = 'co'
    file = open('output/' + fileName + '.' + extension, 'a')
    for line in lines:
     file.write(stringify(line))
    print(lines)

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

def decrypt(file, offset):
    chars = list(file)
    decrypted = []
    for char in chars:
        index = characters.index(char)
        if (index +  offset) > len(characters):
            difference = len(characters) - index
            remainder = index - difference
            index = remainder
        newChar = characters[index - offset]
        decrypted.append(newChar)
    return decrypted

path = input('Please specify file to: ')
offset = int(input('Please set the seed: '))
file = open(path, 'r')
result = decrypt(file.read(), offset)
output(result, 'test', False)