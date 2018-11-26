import base64

encoded_data = base64.b64encode('Encode this text'.encode('utf-8'))
print('Encoded text with base 64 is ', encoded_data)

decoded_data = base64.b64decode(b'RW5jb2RlIHRoaXMgdGV4dA==')
print('Decoded text with base 64 is ', decoded_data)
