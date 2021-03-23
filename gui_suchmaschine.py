"""Creates a simple Tkinter GUI"""
import glob
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Function to look for consecutive ocurrences of strings in the excels and insert them into text

"""def search_excels(codes):
    texts = tk.Text(root, height=500, width=700)
    my_excels = []
    for fil in glob.glob("./*.xlsx"):
        my_excels.append(pd.read_excel(fil, header=2, usecols=(0, 1, 2, 3, 4)))
    for lst in my_excels:  # Loop through all files
        # Test if there are spaces (pruned list)
        lstpr = [x if not isinstance(x, str) else x.replace(
            ' ', '') for x in list(lst["Codes"])]
        # Look for strings in pruned lists
        for i, j in enumerate(lstpr):
            if i == len(lstpr) - len(codes) + 1:  
                break
            if lstpr[i:i + len(codes)] == codes:
                texts.insert(tk.END, lst.iloc[i:i + len(codes)])
                texts.insert(tk.END, fil)
    texts.pack()"""

def search_excels(codes):
    texts = tk.Text(root, height=500, width=700)
    my_excels = []
    my_excels_names = []
    for fil in glob.glob("./*.xlsx"):
        my_excels.append(pd.read_excel(fil, header=2, usecols=(0, 1, 2, 3, 4)))
        my_excels_names.append(fil)
    for idx, lst in enumerate(my_excels):  # Loop through all files
        # Test if there are spaces (pruned list)
        lstpr = [x if not isinstance(x, str) else x.replace(
            ' ', '') for x in list(lst["Codes"])]
        # Look for strings in pruned lists
        for i, j in enumerate(lstpr):
            if i == len(lstpr) - len(codes) + 1:
                break
            if lstpr[i:i + len(codes)] == codes:
                texts.insert(tk.END, lst.iloc[i:i + len(codes)])
                texts.insert(tk.END, my_excels_names[idx])
    texts.pack()

# Function to dynamically generate entries


def spin_function(numcodes):
   
    STRENTER = 'Please enter the codes.' 
    lbl_codes = tk.Label(
        master=root, text=STRENTER, font=('Arial', 16))
    lbl_codes.pack()

    # Creates the entries

    dicents = {}
    for idx in range(int(numcodes)):
        dicents[f"Code_{idx}"] = tk.Entry(width=30)
        dicents[f"Code_{idx}"].pack()

    button = tk.Button(root, text="Search",
                       command=lambda: search_excels(
                           list(map(tk.Entry.get, dicents.values()))))

    button.pack()


# Main loop

root = tk.Tk()
root.title("Code Suchmaschine")

# Task for user to select number of codes

STRSUCH = 'Please select the number of codes you want to look for.'

lbl_numcodes = tk.Label(master=root, text=STRSUCH, font=('Arial', 16))
lbl_numcodes.pack()

# Spinbox for user to select number of codes

spinval = tk.StringVar()
spin_numcodes = ttk.Spinbox(master=root, from_=1.0, to=10.0, textvariable=spinval)
spin_numcodes.pack()

# Button to validate selection in Spinbox

button_spin_numcodes = tk.Button(
    root, text="Submit", command=lambda: spin_function(spin_numcodes.get()))
button_spin_numcodes.pack()

root.mainloop()
