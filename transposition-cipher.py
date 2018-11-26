def split_length(sequence, length):
    return [sequence[i:i+length] for i in range(0, len(sequence), length)]

def encode(key, plain_text):
    order = {
        int(value) : number for (number, value) in enumerate(key)
    }
    cipher_text = ''
    for index in sorted(order.keys()):
        for part in split_length(plain_text, len(key)):
            try:
                cipher_text += part[order[index]]
            except IndexError:
                continue
    
    return cipher_text

print(encode('3214', 'HELLO'))