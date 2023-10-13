import numpy as np
import pandas as pd
from tabulate import tabulate

titanic = pd.read_csv('C:/Users/Asus TUF/Desktop/programmirivanie/Python/5 sem/titanic_with_labels.csv', sep = ' ')
titanic = titanic.drop('Unnamed: 0', axis = 1)

buf = titanic['sex'].isin(['М', 'м', 'Ж', 'ж'])
titanic = titanic[buf]
titanic['sex'] = np.where(np.logical_or(titanic['sex']=='Ж', titanic['sex']=='ж'), 0, 1)

max_row = titanic['row_number'].max()
print(max_row)
titanic['row_number'] = titanic['row_number'].fillna(max_row)

titanic['liters_drunk'] = np.where(np.logical_and(titanic['liters_drunk']<15, titanic['liters_drunk']>=0),
                                   titanic['liters_drunk'], np.nan)
titanic['liters_drunk'] = titanic['liters_drunk'].fillna(titanic['liters_drunk'].mean())

print(tabulate(titanic.head(100), headers = 'keys', tablefmt = 'grid'))


