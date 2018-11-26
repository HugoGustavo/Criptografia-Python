import onetimepad

cipher = onetimepad.encrypt('One Time Cipher', 'random')
print('Cipher text is', cipher)
message = onetimepad.decrypt(cipher, 'random')
print('Plain text is', message)
