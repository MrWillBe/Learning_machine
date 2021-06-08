import numpy as np
import matplotlib as plt
import pandas as pd

data = pd.read_excel('titanic3.xls')
data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

data = data.dropna(axis=0)

print(data['pclass'].value_counts())



