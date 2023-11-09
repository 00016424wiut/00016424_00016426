import pandas as pd
import seaborn as sb
data = pd.read_csv("graduation_dataset.csv")


#data cleaning
print(data.isnull().sum())
data = data.drop_duplicates()
data = data.fillna(0)

