class Affine(object):
    DIE = 128
    KEY = (7, 3, 55)

    def __init__(self):
        pass
    
    def encrypt_char(self, char):
        (K1, K2, KI) = self.KEY
        return chr((K1 * ord(char) + K2) % self.DIE)
    
    def encrypt(self, string):
        return ''.join(map(self.encrypt_char, string))
    
    def decrypt_char(self, char):
        (K1, K2, KI) = self.KEY
        return chr(KI * (ord(char) - K2) % self.DIE)

    def decrypt(self, string):
        return ''.join(map(self.decrypt_char, string))

affine = Affine()
print (affine.encrypt('Affine Cipher'))
print (affine.decrypt(affine.encrypt('Affine Cipher')))