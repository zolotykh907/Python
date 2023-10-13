import numpy

def init_matr(filename):
    f = open(filename, 'r')
    matr = []
    while 1:
        s = f.readline()
        if not s:
            break
        if s == '\n':
            break
        else:
            s = s.replace('\n', '')
            s = (s.split(' '))
            s = list(map(int, s))
            matr.append(s)
    return matr

def proverka_matr(matr1, matr2):
    if len(matr1)==len(matr2) and len(matr1[0]) == len(matr2[0]):
        return 1
    else:
        return 0

def print_matr(matr):
    for i in range(len(matr)):
        stroka = ''
        for elem in matr[i]:
            stroka += str(elem)
            stroka += ' '
        print(stroka)

class Pupa:
    def __init__(self):
        self.count = 0

    def do_work(self, filename1, filename2):
        self.matr1 = init_matr(filename1)
        self.matr2 = init_matr(filename2)
        if proverka_matr(self.matr1, self.matr2):
            matr1, matr2 = self.matr1, self.matr2
            res = []
            for i in range(len(matr1)):
                row = []
                for j in range(len(matr1[0])):
                    row.append(matr1[i][j] + matr2[i][j])
                res.append(row)
            print("Pupa выполнил работу:")
            print_matr(res)
        else:
            raise('Такие матрицы нельзя складывать и вычитать')

    def take_salary(self, n):
        self.count += n

class Lupa:
    def __init__(self):
        self.count = 0
    def do_work(self, filename1, filename2):
        self.matr1 = init_matr(filename1)
        self.matr2 = init_matr(filename2)
        if proverka_matr(self.matr1, self.matr2):
            matr1, matr2 = self.matr1, self.matr2
            res = []
            for i in range(len(matr1)):
                row = []
                for j in range(len(matr1[0])):
                    row.append(matr1[i][j] - matr2[i][j])
                res.append(row)
            print("Lupa выполнил работу:")
            print_matr(res)
        else:
            raise('Такие матрицы нельзя складывать и вычитать')

    def take_salary(self, n):
        self.count += n

class Accountant():
    def give_salary(self, person, num):
        person.take_salary(num)
        print(f'Зарплата работнику {person.__class__.__name__} выплачена в размере {num}$')

p = Pupa()
l = Lupa()
a = Accountant()
a.give_salary(p, 10)
p.do_work('input1.txt', 'input2.txt')
l.do_work('input1.txt', 'input2.txt')
a.give_salary(l, -100)


