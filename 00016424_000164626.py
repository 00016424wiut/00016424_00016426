import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

data = pd.read_csv("graduation_dataset.csv")

# data cleaning
print(data.isnull().sum())
data = data.drop_duplicates()
data = data.fillna(0)

# data information
num_rows, num_columns = data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# data analysis/creating a visualization
print(data.describe())
plt.show()


# min and max value of the dataset
print(data.agg(['min', 'max']))

# tkinter
class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("820x300+500+500")
        self.root.title('User Interface')

        self.mainframe = tk.Frame(self.root, background='#d3e3db')
        self.mainframe.pack(fill='both', expand=True)

        # columns label
        column_options = [
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
        self.set_column_options = ttk.Combobox(self.mainframe, values=column_options)
        self.set_column_options.grid(row=1, column=1, sticky='NWES', pady=8)

        label = tk.Label(self.mainframe, text="Columns", bg='#b1f2c2')
        label.grid(row=1, column=0)

        # functions label
        function_options = [
            "Calculating the average of a column", "Finding the minimum and maximum",
            "Counting the occurrences", "Graph"
        ]
        self.set_function_options = ttk.Combobox(self.mainframe, values=function_options)
        self.set_function_options.grid(row=2, column=1, sticky='NWES', pady=8)

        label2 = tk.Label(self.mainframe, text="Functions", bg='#b1f2c2')
        label2.grid(row=2, column=0)

        # label3 for calculating the occurrences
        label3 = tk.Label(self.mainframe, text="Element for occurrences", bg='#b1f2c2')
        label3.grid(row=3, column=0)
        self.text_box = tk.Text(self.mainframe, height=1)
        self.text_box.grid(row=3, column=1)

        # button result
        button = tk.Button(self.mainframe, text="Result", command=self.button_func)
        button.grid(row=5, column=1, pady=10)

        # text in the center
        self.text = ttk.Label(self.mainframe, text='Choose a column and function', background='#d3e3db',
                              font=('Times New Roman', 20))
        self.text.grid(row=0, column=1)
        self.root.mainloop()

    def button_func(self):
        column = self.set_column_options.get().strip()
        func = self.set_function_options.get().strip().lower()
        element = self.text_box.get("1.0", 'end-1c').strip().lower()

        if func == "calculating the average of a column":
            average = data[column].mean()
            print(f"Average of {column}: {average}")

        elif func == "finding the minimum and maximum":
            minimum = data[column].min()
            maximum = data[column].max()
            print(f"Minimum of {column}: {minimum}")
            print(f"Maximum of {column}: {maximum}")

        elif func == "counting the occurrences":
            x = [i for i in data[column] if i == element]
            print("The element", element, "occurs", len(x), "times")

        elif func == "graph":
            plt.hist(data[column], bins=9, align='right', color='#91e6bb', edgecolor='black')
            plt.show()

if __name__ == "__main__":
    Interface()