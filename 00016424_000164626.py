import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import argparse
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
