from tkinter.filedialog import askopenfilename
import tkinter as tk
import struct

def getFile():
    """
        Uses tkinter to open a file dialog box and allows user selection of a file.
        @return File path seslected through tkinter GUI 
    """
    root = tk.Tk()
    file = askopenfilename(parent=root, title="Select file")
    root.quit()
    root.destroy()

    return(file)


def readBinFile(fileName):
    with open(fileName, mode='rb') as file:
        fileContent = file.read()

    return fileContent





if __name__ == "__main__":
    fileName = getFile()
    print(readBinFile(fileName))
    