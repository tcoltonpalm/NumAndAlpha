"""Creates a program where lists of words or numbers can be alphabetised
    or numerically sorted

"""

import pyperclip



#empty list
a = pyperclip.paste()
items = a.split()
items.sort()


print items

for item in items:
    if item.isdigit():
        print("Number!")
    else: print("Letters!")

pyperclip.copy(str(" ".join(items)))
