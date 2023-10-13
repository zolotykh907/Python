import numpy as np
import random

#1
#arr = np.array([1,2,2,2,3,3,4,4,4,4,5])
arr = np.random.randint(0, 10, 10)
value, counts = np.unique(arr, return_counts=True)
sort_id = np.argsort(counts)
sort_arr = value[sort_id]
res = np.repeat(sort_arr, counts[sort_id])
print('1:', res[::-1])

#2
h = 3
w = 5
arr = np.random.randint(0, 255, (h,w))
#arr = np.array([[1,2,3], [2,3,4], [5,6,7]])
print('2:', *arr)

values, counts = np.unique(arr, return_counts = True)
res = values[counts == 1]
print('Уникальные значения:', res, '\n', 'Количество уникальных значений:', len(res))

#3
win = 3
arr = np.array([1,2,3,4,5,6,7,8,9])
res = [0]*(win-1)
for i in range(win-1, len(arr)):
    begin = i - win + 1
    res.append(np.mean(arr[begin:i+1]))
print('3:', res)

#реализация без циклов(такое себе, менее понятно, чем с циклом)
def f(arr, win):
    a = np.lib.stride_tricks.sliding_window_view(arr, window_shape=win)
    res = np.mean(a, axis=-1)
    return res

res = f(arr, win)
b = list(np.array([0]*(win-1), float))
res = b + list(res)
print("Реализация без циклов:", res)

#4
def f(arr):
    if arr[0]+arr[1] > arr[2]:
        return 1

arr = np.array([[2,2,3], [2,3,7], [6,1,2], [5,6,7]])
r = np.sort(arr, axis = 1)

a = list(map(f, r))
res = np.array(a)
b = r[res != None]

print('4: Можно составить треугольник со следующими сторонами:', *b)