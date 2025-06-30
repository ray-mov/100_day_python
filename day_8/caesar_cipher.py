from pandas.core.array_algos.transforms import shift

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction =  input('Type encode to encrypt, type decode to decrypt: \n').lower()
text = input('Type Your Message: \n').lower()
shift_by = int(input('Type shift number: \n'))


def encrypt(txt,shift_num):
    encrypted_text = ''
    for char in txt:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += alphabet[(index + shift_num) % 25]
    print(encrypted_text)

def decrypt(txt,shift_num):
    decrypted_text = ''
    for char in txt:
        if char in alphabet:
            index = alphabet.index(char)
            to_shift = (index - shift_num)
            if to_shift < 0:
                to_shift -=1
            decrypted_text += alphabet[to_shift]
    print(decrypted_text)

if direction == 'encode':
    encrypt(text,shift_by)
elif direction == 'decode':
    decrypt(text,shift_by)


