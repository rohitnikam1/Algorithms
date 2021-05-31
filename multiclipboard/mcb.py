#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# Saves and loads  multiple pieces of text to the clipboard
#Usage:
# python mcb.py save <keyword>    (saves clipboard to keyword)
# python mcb.py delete <keyword>  (deletes the keyword entry)
# python mcb.py <keyword>         (loads keyword to clipboard)
# python mcb.py list              (loads all keywords to clipboard)
# python mcb.py deleteall         (deletes all entries)

import shelve, pyperclip, sys

mcbshelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower()=='save':
        mcbshelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower()=='delete':
        mcbshelf.pop(sys.argv[2])
        pyperclip.copy(str(list(mcbshelf.items())))

# list keywords
elif sys.argv[1]=='list':
    pyperclip.copy(str(list(mcbshelf.keys())))

# load content
elif sys.argv[1] in mcbshelf:
    pyperclip.copy(mcbshelf[sys.argv[1]])

# delete all entries
elif sys.argv[1]=='deleteall':
    mcbshelf.clear()
    pyperclip.copy(str(list(mcbshelf.items())))

mcbshelf.close()
