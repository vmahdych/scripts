#!/usr/bin/env python3
 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):

    for n in range(shift_amount):
        alphabet.append(alphabet[n])
    
    new_text = ""

    for i in list(plain_text):
        new_text += alphabet[alphabet.index(i) + shift_amount]
    
    print(new_text)


def decrypt(plain_text, shift_amount):
    
    for n in range(shift_amount):
        new = alphabet[::-1]
        new.append(new[n])
    print(new)     

decrypt(text, shift)
#encrypt(text, shift)
