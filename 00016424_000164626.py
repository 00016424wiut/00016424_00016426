import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import argparse as arg
from argparse import ArgumentParser, Namespace
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
data = pd.read_csv("graduation_dataset.csv")

#data exploration
num_rows, num_columns = data.shape
print(f"Number of rows:{num_rows}")
print(f"Number of columns:{num_columns  }")

#data cleaning
print(data.isnull().sum())
data = data.drop_duplicates()
data = data.fillna(0)

#data analysis/creating a visualization
print(data.describe())
plt.show()


#parse


#tkinter
class Interface():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300+4000+500")
        self.root.title('User Interface')
        self.mainframe = tk.Frame(self.root, background='light blue')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Choose a column and row')
        self.text.grid(row=0, column=0)
        self.root.mainloop()
        return

if __name__ == '__main__':
    Interface()