# Caesar Cipher
def inCode ():
    text = str(input("Enter your message: "))
    key = int(input("Encrypted level: "))
    encryption = ""
    for char in text:

        if char.isupper():
            charIndex = ord(char) - ord('A')
            charShift = (charIndex + key) % 26 + ord('A')
            charNew = chr(charShift)
            encryption += charNew
        elif char.islower():
            charIndex = ord(char) - ord('a')
            charShift = (charIndex + key) % 26 + ord('a')
            charNew = chr(charShift)
            encryption += charNew
        else:
            encryption += char
            
    print (encryption)

def desCode ():
    encryption = input ('Enter your cryptogram:')
    text = ''
    for char in encryption:
        if not char.isalpha ():
            continue
        char = char.upper ()
        code = ord (char) - 1
        if code <ord ('A'):
            code = ord ('Z')
        text += chr (code)
    print (text)

inCode()
