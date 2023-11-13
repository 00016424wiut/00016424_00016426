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
        self.root.geometry("500x350+700+700")
        self.root.title('User Interface')

        self.mainframe = tk.Frame(self.root, background='#b1f2c2')
        self.mainframe.pack(fill='both', expand=True)

        options = [
            "Marital status", "Application mode", "Application order", "Course", "Daytime/evening attendance",
            "Previous qualification", "Nationality", "Mother's qualification", "Father's qualification",
            "Mother's occupation", "Father's occupation", "Displaced", "Educational special needs",
            "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder", "Age at enrollment",
            "International", "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)",
            "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)",
            "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)",
            "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)",
            "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)",
            "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)", "Unemployment rate",
            "Inflation rate", "GDP", "Target"
        ]
        self.clicked = tk.StringVar()
        self.clicked.set('')
        drop = tk.OptionMenu(self.root, self.clicked, *options)
        drop.pack()

        label = tk.Label(self.root, textvariable=self.clicked, height=50)
        label.pack()

        self.text = ttk.Label(self.mainframe, text='Choose a column and function', background='#b1f2c2', font=('Times New Roman', 25))
        self.text.grid(row=0, column=0)
        self.root.mainloop()
        return

if __name__ == "__main__":
    Interface()
