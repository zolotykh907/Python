from random import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num', type=int)
args = parser.parse_args()
n = args.num
n=5

def list_generation(n):
    arr = []
    for i in range(n):
        arr.append(random())
    return arr

def bubble_sort(n):
    arr = list_generation(n)
    k = 0
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                a = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
        k+=1
    return arr

print(bubble_sort(n))
                
            
    