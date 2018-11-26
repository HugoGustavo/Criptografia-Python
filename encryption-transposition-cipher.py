import pyperclip

def main():
    my_message = 'Transposition Cipher'
    my_key = 10
    cipher_text = encrypt_message(my_key, my_message)

    print('Cipher text is: ', cipher_text + '|')
    pyperclip.copy(cipher_text)

def encrypt_message(key, message):
    cipher_text = [''] * key

    for column in range(key):
        position = column
        while position < len(message):
            cipher_text[column] += message[position]
            position += key
    return ''.join(cipher_text)

if __name__ == '__main__':
    main()