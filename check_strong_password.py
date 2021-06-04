#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# Strong password checker. Password is defined strong if:
# it is at least 8 characters long
# contains both uppercase and lowercase characters
# has at least one digit

import re, sys


if len(sys.argv) < 2:
    print('Usage: python check_strong_password.py [string]. Enter password.')
    sys.exit()

password = str(sys.argv[1])

upper = re.compile(r'[A-Z]')
lower = re.compile(r'[a-z]')

if len(password) < 8:
    print('Password must be at least 8 characters long.')
elif upper.search(password) is None:
    print('Password must contain at least one uppercase character.')
elif lower.search(password) is None:
    print('Password must contain at least one lowercase character.')
elif password.isalpha():
    print('Password must contain at least one digit.')
else:
    print('Strong password')
