'''
Retrieves file requests from an HTML page, and loads up File Selector UI. Returns the selected filepath to the HTML's JS as a string
'''

import sys, os, tkinter
from tkinter import *
from tkinter import filedialog

print('Starting Program')

def getUserFile():
    localTk = Tk()
    localTk.withdraw()
    localTk.wm_attributes("-topmost", 1)
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Desktop"))
    return(filepath)
    

filepath = getUserFile()
sys.exit(filepath)