# from string import maketrans

rot13trans = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
)

def rot13(text):
    return text.translate(rot13trans)

def main():
    text = "ROT13 Algorithm"
    print (rot13(text))

if __name__=="__main__":
    main()