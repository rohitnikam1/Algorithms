#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# An insecure password locker program

passwords = {'xyz@gmail.com': 'password-gmail',
             'facebook': 'abc'
            }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'Password for the account is copied.')
else:
    print('Account not found in database. Please make an entry.')
