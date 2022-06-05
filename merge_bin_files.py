"""
Merges bin files
"""






import os
from tkinter  import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames

Tk().withdraw()             # We don"t want a full GUI, so keep the root window from appearing
files = askopenfilenames()  # Show an "Open" dialog box and return the path to the selected file

word = "/"

fileName = "total.bin"

try:
    dateStr = os.path.basename(os.path.dirname(files[0]))
    # print(dateStr)

    indexOfWord = files[0].rfind(word)
    fileName = files[0][0:indexOfWord] + "/" + dateStr + " - " + "total.bin"
except:
    pass


with open(fileName, "ab") as f:
    newFile = bytes()

    for file in files:
        newFile += open(file, "rb").read()

    f.write(newFile)