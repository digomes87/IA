import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


date_path = 'BikeDataSet/hour.csv'
df = pd.read_csv(date_path)
df.head()

ime = df[:24*10].plot(x= 'dteday', y='cnt')


dummy_fields = ['season', 'mnth', 'hr', 'weekday']

for each in dummy_fields:
    dummies = pd.get_dummies(df[each], prefix = each, drop_first=False)
    df = pd.concat([df, dummies], axis = 1)

colunas_para_deletar = ["instant", "dteday", "season", "atemp"]
data = df.drop(colunas_para_deletar, axis=1)
data.head()

print(df)
