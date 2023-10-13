import argparse
import numpy as np

def init_arr(filename):
    f = open(filename, 'r')
    s = f.readline()
    s = s.replace('\n', '')
    s = (s.split(' '))
    s = list(map(int, s))
    return s

parser = argparse.ArgumentParser()
parser.add_argument('file1', type=str)
parser.add_argument('file2', type=str)
parser.add_argument('p', type=float)
args = parser.parse_args()

filename1 = args.file1
filename2 = args.file2
p = args.p

real = np.array(init_arr(filename1))
sint = np.array(init_arr(filename2))

if len(real) != len(sint):
    raise('Массивы разной длины')
if p > 1 or p < 0:
    raise('Неправильная вероятность')

koeff = np.random.random(len(real))
koeff = np.where(koeff < p, 0, 1)
res = np.where(koeff, real, sint)

print(res)