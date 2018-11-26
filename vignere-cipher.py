import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt_message(key, message):
    return translated_message(key, message, 'encrypt')

def decrypt_message(key, message):
    return translated_message(key, message, 'decrypt')

def translated_message(key, message, mode):
    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if ( num != -1):
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])
            num %= len(LETTERS)

            if( symbol.isupper() ):
                translated.append(LETTERS[num])
            elif( symbol.islower() ):
                translated.append(LETTERS[num].lower())
            key_index += 1
        
            if ( key_index == len(key) ):
                key_index = 0
        else:
            translated.append(symbol)
    
    return ''.join(translated)  

def main():
    my_message = 'This is basic implementation of Vignere Cipher'
    my_key = 'PIZZA'
    my_mode = 'encrypt'

    translated = ''
    if my_mode == 'encrypt':
        translated = encrypt_message(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, my_message)
    
    print('%sed message: ' % (my_mode.title()))
    print(translated)
    print()

if __name__ == '__main__':
    main()