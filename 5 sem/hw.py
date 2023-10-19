import numpy as np
import pandas as pd
from tabulate import tabulate

def num1():
    col = 5
    row = 10
    n = 0.3

    data = np.random.random((row, col))
    data_frame = pd.DataFrame(data)

    buf = data_frame[data_frame>n]
    res = buf.mean(axis = 1)
    data_frame['Среднее значение'] = res
    print('1:\n', tabulate(data_frame, headers = 'keys', tablefmt = 'grid'), sep = '')
    #print('Средние значения в строках:\n', res.to_string(), sep = '')

def num2():
    filename = 'C:/Users/Asus TUF/Desktop/programmirivanie/Python/5 sem/wells_info1.csv'
    data_frame = pd.read_csv(filename)
    #data_frame = data_frame.set_index('API')

    data_frame['CompletionDate'] = pd.to_datetime(data_frame['CompletionDate'])
    data_frame['FirstProductionDate'] = pd.to_datetime(data_frame['FirstProductionDate'])
    data_frame['PermitDate'] = pd.to_datetime(data_frame['PermitDate'])
    data_frame['SpudDate'] = pd.to_datetime(data_frame['SpudDate'])

    data_frame['Время добычи (в месяцах)'] = ((data_frame['CompletionDate'] - data_frame['SpudDate']) / np.timedelta64(30, 'D')).astype(int)
    print('2:\n', tabulate(data_frame, headers = 'keys', tablefmt = 'grid'), sep = '')

def num3():
    filename = 'C:/Users/Asus TUF/Desktop/programmirivanie/Python/5 sem/wells_info_na.csv'
    data_frame = pd.read_csv(filename)

    # data_frame['LatWGS84'] = data_frame['LatWGS84'].fillna(data_frame['LatWGS84'].median())
    # data_frame['LonWGS84'] = data_frame['LonWGS84'].fillna(data_frame['LonWGS84'].median())

    col_id = data_frame.select_dtypes(include=['float64']).columns
    data_frame[col_id] = data_frame[col_id].fillna(data_frame[col_id].median())
    col_id_not_number = data_frame.select_dtypes(exclude=['float64']).columns
    for i in col_id_not_number:
        value = data_frame[i].mode()[0]
        data_frame[i] = data_frame[i].fillna(value)

    print('3:\n', tabulate(data_frame, headers='keys', tablefmt='grid'), sep='')

num1()





