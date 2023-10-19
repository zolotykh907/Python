from random import randint 
from math import pi, sqrt
import os

#1
def sum(a):  
    res = 0
    l = len(str(a))
    for i in range(0, l):
        res += a//(10**i)%10
    return res

a = randint(100, 999);
print("1:", a, sum(a))

#2
a = randint(0, 2147483647)
print("2:", a, sum(a))

#3
r = int(input("3: vvedite radius:"))
s = 4*pi*r**2
v = (4*pi*r**3)/3
print("s=", s, "v=", v)

#4
year = int(input("4: vvedite god:"))
if year%400==0 or year%4==0:
    print('viskosniy')
elif year%100==0:
    print('ne visokosniy')
else:
    print('ne visokosniy')
    
#5
def prime(b):
    res = [1]
    for i in range(1, b+1):
        count = 0
        for j in range(1, i):
            if i%j==0:
                count+=1
            if count == 2:
                break
        if count==1:
            res.append(i)
    return res
        
b = int(input('5: vvedite diapazon:'))
print(prime(b))

#6
def summa(x, y):
    res = x
    for i in range(y):
        res = x + x/10
        x=res
    return res

x = int(input("6: vvedite money:"))
y = int(input("vvedite years:"))
print(int(summa(x, y)))

#7
path = input("7: vvedite path:")
print("all files:")
for root, dirnames, filenames in os.walk(path):
    for f in filenames:
        print(f)
            
            
        
            
    


