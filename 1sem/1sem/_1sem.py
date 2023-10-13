def f1():
    class MyClass():
        def one():
             print(1)
        def two():
             print(2)

    a = MyClass
    a.one()
    a.two()

def f2():
    l = [1,2,3,4,5]
    for i in l:
        print(i, end = ' ')
        
#f1()
#f2()

