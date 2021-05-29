#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# Extracts (USA) phone numbers and email addresses on the clipboard 
# Select all the webpage (Ctrl+A) and copy (Ctrl+C) then run this script


import re, pyperclip

reg_phone = re.compile(r'''(
                 (\d{3}|\(\d{3}\))?       # area code
                 (\s|-|\.)?               # separator
                 (\d{3})                  # first 3 digits
                 (\s|-|\.)?               # separator
                 (\d{4})                  # last 4 digits
                 (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                 )''', re.VERBOSE)


reg_email = re.compile(r'''(
                 [a-zA-Z0-9._+-]+          # usename
                 @                        # @ character
                 [a-zA-Z0-9.-]+           # domain name
                 (\.[a-zA-Z]{2,4})        # dot something
                 )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in reg_phone.findall(text):
    num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        num += '  x' + groups[8]
    matches.append(num)


for groups in reg_email.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    list_ = '\n'.join(matches)
    pyperclip.copy(list_)
    print(f'Matches copied to clipboard:\n {list_}')
else:
    print('No phone numbers or email addresses found')
