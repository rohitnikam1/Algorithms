#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# Saves and loads  multiple pieces of text to the clipboard
#Usage:
# mcb.pyw save <keyword> (saves clipboard to keyword)
# mcb.pyw <keyword> (loads keyword to clipboard)
# mcb.pyw list (loads all keywords to clipboard)

import shelve, pyperclip, sys

mcbshelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower()=='save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()

# list keywords
elif sys.argv[1]=='list':
    pyperclip.copy(str(list(mcbshelf.keys())))

# load content
elif sys.argv[1] in mcbshelf:
    pyperclip.copy(mcbshelf[sys.argv[1]])

mcbshelf.close()
