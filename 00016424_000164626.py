import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

data = pd.read_csv("graduation_dataset.csv")

# data cleaning
print(data.isnull().sum())
data = data.drop_duplicates()
data = data.fillna(0)

# data analysis/creating a visualization
print(data.describe())
plt.show()


# tkinter
class Interface():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300+500+500")
        self.root.title('User Interface')

        self.mainframe = tk.Frame(self.root, background='#d3e3db')
        self.mainframe.pack(fill='both', expand=True)

        # label1
        column_options = [
            "All", "Marital status", "Application mode", "Application order", "Course", "Daytime/evening attendance",
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
        self.set_column_options.grid(row=1, column=1, sticky='NWES', pady=10)

        label = tk.Label(self.mainframe, text="Columns", bg='#b1f2c2', )
        label.grid(row=1, column=0)

        # label2
        function_options = [
            "Number of rows and columns", "Calculating the average of a column", "Find the minimum and maximum",
            "Counting the occurrences", "Graph"
        ]

        self.set_function_options = ttk.Combobox(self.mainframe, values=function_options)
        self.set_function_options.grid(row=2, column=1, sticky='NWES', pady=10)

        label2 = tk.Label(self.mainframe, text="Functions", bg='#b1f2c2', )
        label2.grid(row=2, column=0)

        #button
        set_button = ttk.Button(self.mainframe, text="Result", command=button_func)
        set_button.grid(row=3, column=1, pady=10)



        self.text = ttk.Label(self.mainframe, text='Choose a column and function', background='#d3e3db', font=('Times New Roman', 20))
        self.text.grid(row=0, column=1)
        self.root.mainloop()
def button_func(set_function_options):
    func = set_function_options.get().strip().lower()

    if func in ("Number of rows and columns"):
        num_rows, num_columns = data.shape
        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_columns}")

    elif func in ("Calculating the average of a column"):
        df=pd.DataFrame()
        df["average"] = df[][1:].mean()
        print(df["average"])


if __name__ == "__main__":
    Interface()