import re
from random import randint
#1
string = input("1: vvedite stroku:")
if string == string[::-1]:
    print(string, "- polindrom")
else:
    print(string, "- ne polindrom")
    
#2
string = input("2: vvedite stroku:").split()
print(len(max(string, key=len)))

#3
arr = [randint(0, 100) for i in range(10)]
k1, k2 = 0, 0
for i in arr:
    if i%2==0:
        k1+=1
    else:
        k2+=1
print("3:", arr, "\n", "chetnih - ", k1, "\n", "nechentih -", k2)

#4
slovar = {'a':'A', 'b':'B', 'c':'C'}
stroka = 'a b c.'.split(' ')

for i in range(len(stroka)):
    stroka[i]=slovar[stroka[i]]
print("4:", ' '.join(stroka))
#5
n = int(input("5: vvedite, do kakogo chisla vichislyat: "))
def fib(n):
    if(n==1 or n==2):
        return 1
    return fib(n-1)+fib(n-2)
print(fib(n))

#6
f = open('input.txt', 'r')
fi = s = f.read()
a = re.split(' |\n', fi)
l = sum(len(s) for s in a)
space = s.count(' ')
print("6: strok - ", s.count('\n')+1)
print("slov - ", len(a))
print("bukv - ", l)
print("simvolov - ", l+space)

7
first = int(input("7: vvedite pervoe chislo progressii: "))
last = int(input("vvedite granicu: "))
step = int(input("vvedite shag: "))
arr = [first]
while(arr[-1]<last):
    a=arr[-1]*step
    arr.append(arr[-1]*step)
    
print(arr[:-1])