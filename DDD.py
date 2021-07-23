# Caesar Cipher
def inCode ():
    text = input ("Enter your message:")
    encryption = ''
    for char in text:
        if not char.isalpha ():
            continue
        char = char.upper ()
        code = ord (char) + 1
        if code> ord ('Z'):
            code = ord ('A')
        encryption += chr (code)

    print (encryption)

# Caesar Cipher - decrypt a message
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


inCode ()
desCode ()