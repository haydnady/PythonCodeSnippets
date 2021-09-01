"""
Renames files of media series
"""


import os
from tkinter  import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames


Tk().withdraw()             # We don't want a full GUI, so keep the root window from appearing
files = askopenfilenames()  # Show an "Open" dialog box and return the path to the selected file

word = "Episode"

for file in files:
    if word in file:
        indexOfWord = file.find(word)
        newFileName = file[0:indexOfWord] + "- S21E" + file[indexOfWord+len(word)+1:]
        # print(newFileName)
        os.rename(file, newFileName)
