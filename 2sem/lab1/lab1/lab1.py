def start():
    ''' Начало программы. global fin, fout, m1, m2 - создание глобальных переменных, чтобы работать с ними в разных функциях, инициализация двух матриц(init_matr()),
    проверка матриц на соответствие размерностей(proverka()), вывод результирующей матрицы(print_matr()), умножение матриц(mul_matr())
    
    Переменные
    ----------
    file_in : str 
        Cтрока с названием/путем файла для чтения
    file_out : str
        Строка с названием/путем файла для записи
    fin и fout открвают файлы для чтения и записи матриц соответсвенно, 
    m1 : [[int]]
        Первая матрица, двумерный массив интов
    m2 : [[int]]
        Вторая матрица, двумерный массив интов
    
    Возвращает
    ----------
    0, конец программы
    '''
    global fin, fout, m1, m2
    
    file_in = input("Введите название файла с матрицами: ")
    file_out = input("Введите файл, куда записать результат: ")
    fin = open(file_in, 'r')
    fout = open(file_out, 'w')
    
    m1, m2 = [], []
    init_matr(m1)
    init_matr(m2)
    
    
    if(proverka()):
        print_matr(mul_matr())
    else:
        fout.write("Матрицы неправильные")
    
    return 0
    
def init_matr(arr):
    '''Чтение матриц
    
    Переменные
    ----------
    s : str
        считываем каждую строку из файла, обрабатываем ее, делаем из нее список интов(значений матрицы), добавляем в массив
    Параметры
    ---------
    arr : [[int]]
        двумерный массив интов, куда будет записана матрица  
    '''
    while 1:
        s = fin.readline()
        if not s:
            break
        if s == '\n':
            break
        else:
            s = s.replace('\n', '')
            s = (s.split(' '))
            s = list(map(int, s))
            arr.append(s)

def proverka():
    '''
    Выполняется проверка матриц на соответствие размерностей: число столбцов первой матрицы должно совпадать с числом строк второй
    Возвращает
    ----------
    1, если условие вфполняется
    0 иначе
    '''
    if (len(m1[0])==len(m2)):
        return 1
    return 0

def mul_matr():
    '''
    Функция умножения матрицб, вычисляем кажддый элемент результирующей матрицы в тройном цикле
    
    Переменные
    ----------
    res : [[int]]
        создается двумерный массив интов (количество строк первой матрицы X количество столбцов второй)
    
    Возвращает
    ----------
    двумерный массив, искомую матрицу
    '''
    res = [[0]]*len(m1)
    for i in range(len(m1)):
        res[i]=[0]*len(m2[0])
    

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                res[i][j]+=m1[i][k]*m2[k][j]
    
    return res


def print_matr(arr):
    '''
    Выводит матрицу в файл, построчно
    
    Переменные
    ----------
    stroka : str
        изначальо пустая, конкатинацией добваляем элементы из массива интов, преобразуя их в строку, между каждым элементом добавляем пробелы
    '''
    for i in range(len(arr)):
        stroka = ''
        for elem in arr[i]:
            stroka += str(elem)
            stroka += ' '
        fout.write(stroka)
        fout.write('\n')
        

start()
