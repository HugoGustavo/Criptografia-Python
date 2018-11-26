def encrypt(text, s):
    result = ""
    # tranverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65 )
        elif char.islower():
            result += chr((ord(char)+s-97)%26+97)
        else:
            result += char
    return result

text = "CEASER CIPHER DEMO"
s = 4

print ("Plain text   : ", text)
print ("Shift pattern: ", str(s))
print ("Cipher       : ", encrypt(text, s))

message = 'GIEWIV GMTLIV HIQS' # encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0 :
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))