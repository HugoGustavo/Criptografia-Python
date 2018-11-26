import math, pyperclip

def main():
    my_message = 'Toners raiCntisippo'
    my_key = 6
    plain_text = decrypt_message(my_key, my_message)
    print('The plain text is Transposition Cipher')

def decrypt_message(key, message):
    number_of_columns = math.ceil(len(message) / key)
    number_of_rows = key
    number_of_shaded_boxes = ( number_of_columns * number_of_rows ) - len(message)
    plain_text = [''] * number_of_columns
    column = 0 
    row = 0
    for symbol in message:
        plain_text[column] += symbol
        column += 1
        if ( column == number_of_columns ) or (column == number_of_columns -1 and row >= number_of_rows -number_of_shaded_boxes):
            row += 1
    return ''.join(plain_text)

if __name__ == '__main__':
    main()
