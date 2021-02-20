import os
from tkinter.filedialog import askopenfilename

def selectFile():
    path=askopenfilename(title='Select a .txt file', filetypes=[('TXT', '*.txt')])

    try:
        File=open(path,'r', encoding='utf-8')
        lines = File.readlines()
        print("Content:")
        for line in lines:
            print(line,end="")
        File.close()
        return lines
        
    except:
        print("Fail to Open the file, please try again.")
        return None

    
    

#selectFile()


def encrypt(s):
    key = {'!': ')', '"': '{', '#': 'a', '$': '!', '%': 'w', '&': ';', "'": 'o', '(': '4', ')': 'X', '*': 'R', '+': 'b', ',': 'S', '-': '^', '.': 'P', '/': '.', '0': 'Y', '1': 'z', '2': ']', '3': 'j', '4': 'W', '5': '3', '6': 't', '7': 'T', '8': 'p', '9': '~', ':': "'", ';': 'U', '<': '1', '=': 'J', '>': ',', '?': 'u', '@': 'g', 'A': 'H', 'B': '+', 'C': 'C', 'D': 'v', 'E': '}', 'F': '@', 'G': '&', 'H': 'M', 'I': 'c', 'J': '$', 'K': 'N', 'L': 'l', 'M': '/', 'N': '9', 'O': 'F', 'P': 'Q', 'Q': '*', 'R': '?', 'S': '2', 'T': '<', 'U': 'y', 'V': 'x', 'W': 'q', 'X': 'n', 'Y': ':', 'Z': '=', '[': '5', '\\': '(', ']': '[', '^': 'm', '_': '-', '`': '|', 'a': 'f', 'b': '8', 'c': 'D', 'd': '0', 'e': 'e', 'f': 'r', 'g': 'E', 'h': 'h', 'i': '_', 'j': 'O', 'k': '%', 'l': '\\', 'm': '#', 'n': 'G', 'o': '6', 'p': 'L', 'q': '7', 'r': 'Z', 's': '"', 't': '`', 'u': 'I', 'v': '>', 'w': 'A', 'x': 's', 'y': 'K', 'z': 'd', '{': 'B', '|': 'i', '}': 'k', '~': 'V'}
    if 33<=ord(s)<=126:
        return key[s]
    else:
        return s

def decode(s):
    opKey = {')': '!', '{': '"', 'a': '#', '!': '$', 'w': '%', ';': '&', 'o': "'", '4': '(', 'X': ')', 'R': '*', 'b': '+', 'S': ',', '^': '-', 'P': '.', '.': '/', 'Y': '0', 'z': '1', ']': '2', 'j': '3', 'W': '4', '3': '5', 't': '6', 'T': '7', 'p': '8', '~': '9', "'": ':', 'U': ';', '1': '<', 'J': '=', ',': '>', 'u': '?', 'g': '@', 'H': 'A', '+': 'B', 'C': 'C', 'v': 'D', '}': 'E', '@': 'F', '&': 'G', 'M': 'H', 'c': 'I', '$': 'J', 'N': 'K', 'l': 'L', '/': 'M', '9': 'N', 'F': 'O', 'Q': 'P', '*': 'Q', '?': 'R', '2': 'S', '<': 'T', 'y': 'U', 'x': 'V', 'q': 'W', 'n': 'X', ':': 'Y', '=': 'Z', '5': '[', '(': '\\', '[': ']', 'm': '^', '-': '_', '|': '`', 'f': 'a', '8': 'b', 'D': 'c', '0': 'd', 'e': 'e', 'r': 'f', 'E': 'g', 'h': 'h', '_': 'i', 'O': 'j', '%': 'k', '\\': 'l', '#': 'm', 'G': 'n', '6': 'o', 'L': 'p', '7': 'q', 'Z': 'r', '"': 's', '`': 't', 'I': 'u', '>': 'v', 'A': 'w', 's': 'x', 'K': 'y', 'd': 'z', 'B': '{', 'i': '|', 'k': '}', 'V': '~'}
    if 33<=ord(s)<=126:
        return opKey[s]
    else:
        return s


def addNewFile(lines):
    File = open('test2.txt','w')
    for line in lines:
        File.write(line)

    File.close()

def main():
    line = "123456[{}]3[{}]25[{}]"
    newline = ''
    for i in line:
        newline += encrypt(i)
    
    print(newline)
main()


def get_id(x):
    id = ''
    for j in range(6):
        id += str(random.randint(0,9))

    if id not in ids:
           ids.append(id+s)
    
    return ids


'''import random

a = []
b = []
for i in range(33,127):
    a.append(chr(i))
    b.append(chr(i))
key = dict()
for i in range(33-33,127-33):
    index1 = i
    index2 = random.randint(0,len(b)-1)
    key.update({a[index1]:b[index2]})
    b.remove(b[index2])

print(key)
print()
opKey = dict()
for i in key:
    opKey.update({key[i]:i})
print(opKey)'''

