import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import argparse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *

data = pd.read_csv("graduation_dataset.csv")


#data cleaning
print(data.isnull().sum())
data = data.drop_duplicates()
data = data.fillna(0)

#data analysis/creating a visualization
print(data.describe())
plt.show()

#tkinter
def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter Example")

# Create and place widgets
label = tk.Label(window, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()