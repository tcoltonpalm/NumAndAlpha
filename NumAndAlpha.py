"""Creates a program where lists of words or numbers can be alphabetised
    or numerically sorted

"""

import pyperclip


#empty list
a = pyperclip.paste()
items = a.split()

print(items)

for item in items:
    if item.isdigit():
        print("Number!")
    else: print("Letters!")