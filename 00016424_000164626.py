import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import argparse
import tkinter as tk

data = pd.read_csv("graduation_dataset.csv")


#data cleaning
print(data.isnull().sum())
data = data.drop_duplicates()
data = data.fillna(0)

#data analysis/creating a visualization
print(data.describe())
data['Martial status'].value_counts().plot(kind='bar')
plt.show()

#user interface
window = tk.Tk()
label = tk.Label(window, text="Welcome to the site!")
label.pack()
window.mainloop()


parser = argparse.ArgumentParser(description='Sample CLI using argparse')
parser.add_argument("name", help="Your name")
parser.add_argument("age", help="Your age", type=int)
args = parser.parse_args()
print(f"Hello, {args.name}. You are {args.age} years old.")
