import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num', type=int)
args = parser.parse_args()
n = args.num
mas =[]

def pascal(arr):
    buff = copy.copy(arr)
    for i in range(1, len(arr)):
        buff[i]=(arr[i-1]+arr[i])
    buff.append(1)
    mas.append(buff)
    return buff

arr = [1]
mas.append([1])

for i in range(n):
    arr=pascal(arr)

last = mas[-1]
width_num = len(str(max(last)))+1 
width_last_line = width_num * len(last)

for i in mas:
    string = ""

    for j in i:
        num_str = str(j)
        string += num_str + ' ' * (width_num - len(num_str))

    print(string.center(width_last_line))
