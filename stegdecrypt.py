#!/usr/bin/env python
# StegDecrypt 1.0.0 Desenvolvido por Pedro Nogueira - Hacking Brasil

import getopt
import sys
import subprocess
import time
import io

sf = 0
wordlist = "/usr/share/wordlists/rockyou.txt"

optlist , args = getopt.getopt(sys.argv[1:],'f:w:')


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

for (op,arg) in optlist:
    if op == "-f":
        sf = arg
    if op == "-w":
        wordlist = arg        

if sf == 0:
    print('Default usage : stegdecrypt.py -f <stegofile> -w <wordlist>')
    sys.exit(2)
if wordlist == "/usr/share/wordlists/rockyou.txt":
    print('assuming default file wordlist /usr/share/wordlists/rockyou.txt')

l = len(open(wordlist, encoding='utf-8', errors='replace').readlines())+1

progress(0,l)
with open(wordlist, encoding='utf-8', errors='replace') as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = fp.readline()
       out = subprocess.getoutput("steghide extract -sf " + sf.strip() + " -p '" + line.strip()+"' -f")
       cnt += 1
       progress(cnt,l,'Searching...')

       if 'could not extract' not in out:
            print("We find the passphrase ! it`s : \033[1;32;40m" + line.strip() )
            if input('Do You Want To Continue? ') != 'y':
                break
