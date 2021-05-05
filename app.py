import os
from convert import create_report

from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()
print('Waiting for file selection...')
filename = askopenfilename()
output = os.path.join(os.path.split(filename)[0], 'converted_report.csv')

create_report(filename, output)
