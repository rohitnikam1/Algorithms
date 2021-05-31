#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# An insecure password locker program

import sys, shelve, pyperclip

shelf_file = shelve.open('multiclipboard/mcb')
passwords = shelf_file['passwords']
shelf_file.close()

print(passwords)

if len(sys.argv) < 2:
    print('Usage: python pw.py [account]. Enter account.')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'Password for the {account} account is copied.')
else:
    print('Account not found in database. Please make an entry in the shelf file.')
