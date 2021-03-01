
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

import lasio
las = lasio.read(file_path)
las.keys()
las.curves

