#!/usr/bin/env python3
# Caesar Cipher
def inCode ():
    text = str(input("Enter your message: "))
    key = int(input("Encrypted level: "))
    encryption = ""
    for char in text:

        if char.isupper():
            if not char.isalpha ():
                continue
            charIndex = ord(char) - ord('A')
            charShift = (charIndex + key) % 26 + ord('A')
            charNew = chr(charShift)
            encryption += charNew
        elif char.islower():
            charIndex = ord(char) - ord('a')
            charShift = (charIndex + key) % 26 + ord('a')
            charNew = chr(charShift)
            encryption += charNew
        #Encrypted numbers
        #elif char.isdigit():
        #    charNew = (int(char) + key) % 10
        #    encryption += str(charNew)
        else:
            encryption += char
            
    print (encryption)

def desCode ():
    text = str(input("Enter your cryptogram: "))
    key = int(input("Encrypted level: "))
    encryption = ""
    for char in text:

        if char.isupper():
            if not char.isalpha ():
                continue
            charIndex = ord(char) - ord('A')
            charShift = (charIndex - key) % 26 + ord('A')
            charNew = chr(charShift)
            encryption += charNew
        elif char.islower():
            charIndex = ord(char) - ord('a')
            charShift = (charIndex - key) % 26 + ord('a')
            charNew = chr(charShift)
            encryption += charNew
        #Encrypted numbers
        #elif char.isdigit():
        #    charNew = (int(char) - key) % 10
        #    encryption += str(charNew)
        else:
            encryption += char
            
    print (encryption)
inCode()
desCode()