import math
import time
import random
import string


chars = string.ascii_letters + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)

encrypt_text = input("Enter text to encrypt: ")
encrypted_text = ""

for text in encrypt_text:
    index = chars.index(text)
    encrypted_text += key[index]
print(encrypted_text)

# decrypt
decrypt_text = input("Enter text to decrypt: ")
decrypted_text = ""

for text in decrypt_text:
    index = key.index(text)
    decrypted_text += chars[index]
print(decrypted_text)
