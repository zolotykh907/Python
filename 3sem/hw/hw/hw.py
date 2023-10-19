# class Item:
#     def __init__(self, count=3, max_count=16):
#         self._count = count
#         self._max_count = 16
        
#     def update_count(self, val):
#         if val > self._max_count or val < 0:
#             raise('Perepolnenie')
        
#     def __imul__(self, num):
#         self.update_count(num*self._count)
#         self._count *= num
#         return self
    
#     def __iadd__(self, num):
#         self.update_count(num+self._count)
#         self._count += num
#         return self
    
#     def __isub__(self, num):
#         self.update_count(self._count-num)
#         self._count -= num
#         return self

#     def __mul__(self, num):
#         return self._count*num
    
#     def __add__(self, num):
#         return self._count+num
    
#     def __sub__(self, num):
#         return self._count-num
    
#     def __eq__(self, num):
#         if self._count==num:
#             return 1
#         return 0
    
#     def __lt__(self, num):
#         if self._count<num:
#             return 1
#         return 0
    
#     def __gt__(self, num):
#         if self._count>num:
#             return 1
#         return 0
#     def __ge__(self, num):
#         if self._count>=num:
#             return 1
#         return 0
#     def __le__(self, num):
#         if self._count<=num:
#             return 1
#         return 0
    
# it = Item()
# print(it + 3)
# print(it - 1)
# print(it * 20)
# it *= 5
# print(it._count)
# it -= 4
# print(it._count)
# it += 3
# print(it._count)
# print(it<2)
# it+=1
# print(it._count)



# class Fruit(Item):
#     def __init__(self, ripe=True, **kwargs):
#         super().__init__(**kwargs)
#         self._ripe = ripe

# class Food(Item):
#     def __init__(self, saturation, **kwargs):
#         super().__init__(**kwargs)
#         self._saturation = saturation
        
#     def eatable(self):
#         return self._saturation > 0

# class Apple(Fruit, Food):
#     def __init__(self, ripe = True, count=1, max_count=32, color='green', saturation=10):
#         super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
#         self._color = color

#     def color(self):
#         return self._color
    
#     def eatable(self):
#         return super().eatable and self._ripe
    

# class Mandarin(Fruit, Food):
#     def __init__(self, ripe = True, count = 1, max_count = 32, color = 'orange', saturation = 5):
#         super().__init__(ripe = ripe, count = count, max_count = max_count, saturation = saturation)
#         self._color = color
        
#     def color(self):
#         return self._color
    
#     def eatable(self):
#         return super().eatable and self._ripe
    
# class Banana(Fruit, Food):
#     def __init__(self, ripe = True, count = 1, max_count = 32, color = 'yellow', saturation = 20):
#         super().__init__(ripe = ripe, count = count, max_count = max_count, saturation = saturation)
#         self._colot = color
        
#     def color(self):
#         return self._color
    
#     def eatable(self):
#         return super().eatable and self._ripe
    
# class Potato(Food):
#     def __init__(self, fresh = True, count = 5, max_count = 64, color = 'brown', saturation = 50):
#         super().__init__(count = count, max_count = max_count, saturation = saturation)
#         self._color = color
#         self._fresh = fresh
        
#     def color(self):
#         return self._color
    
#     def fresh(self):
#         return self._fresh
    
#     def eatable(self):
#         return super().eatable and self._fresh
    
# class Tomato(Food):
#     def __init__(self, fresh = True, count = 10, max_count = 40, color = 'red', saturation = 40):
#         super().__init__(count = count, max_count = max_count, saturation = saturation)
#         self._color = color
#         self._fresh = fresh
        
#     def color(self):
#         return self._color
    
#     def fresh(self):
#         return self._fresh
    
#     def eatable(self):
#         return super().eatable and self._fresh
   
# a = Apple()
# print(a+1)

# class Inventory:
#     def __init__(self, _length):
#         self.length = _length
#         self.inventory = self.length*[None]

#     def show_elem(self, id):        
#         return self.inventory[id].__dict__
    
#     def push_elem(self, id, elem):
#         if isinstance(elem, Food) and elem.eatable:
#             if self.inventory[id] is None:
#                 self.inventory[id] = elem
#             else:
#                 print
#             return self
#         else:
#             print('eto nelzya polojit v inventar')     
        



# a = Inventory(10)
# b = Apple()
# a.push_elem(1, b)
# print(a.show_elem(1))

# import numpy as np
# import pandas as pd
# from tabulate import tabulate
#
# def num1():
#     col = 5
#     row = 10
#     n = 0.3
#
#     data = np.random.random((row, col))
#     data_frame = pd.DataFrame(data)
#
#     buf = data_frame[data_frame>n]
#     res = buf.mean(axis = 1)
#     data_frame['Среднее значение'] = res
#     print('1: Начальная таблица:\n', tabulate(data_frame, headers = 'keys', tablefmt = 'grid'), sep = '')
#     #print('Средние значения в строках:\n', res.to_string(), sep = '')
#
# def num2():
#     filename = 'C:/Users/Asus TUF/Desktop/programmirivanie/Python/5 sem/wells_info1.csv'
#     data_frame = pd.read_csv(filename)
#     #data_frame = data_frame.set_index('API')
#
#     data_frame['CompletionDate'] = pd.to_datetime(data_frame['CompletionDate'])
#     data_frame['FirstProductionDate'] = pd.to_datetime(data_frame['FirstProductionDate'])
#     data_frame['PermitDate'] = pd.to_datetime(data_frame['PermitDate'])
#     data_frame['SpudDate'] = pd.to_datetime(data_frame['SpudDate'])
#
#     #res = ((data_frame['CompletionDate'] - data_frame['SpudDate']) / np.timedelta64(30, 'D')).astype(int)
#     #res = pd.DataFrame(res, columns=["Количество месяцев"])
#     data_frame['Время добычи (в месяцах)'] = ((data_frame['CompletionDate'] - data_frame['SpudDate']) / np.timedelta64(30, 'D')).astype(int)
#     print('1:\n', tabulate(data_frame, headers = 'keys', tablefmt = 'psql'), sep = '')
#
# def num3():
#     filename = 'C:/Users/Asus TUF/Desktop/programmirivanie/Python/5 sem/wells_info_na.csv'
#     data_frame = pd.read_csv(filename)
#     data_frame = np.where(data_frame.dtypes == np.float64, data_frame.fillna(data_frame.mean(axis = 1)), data_frame)
#
#     print(tabulate(data_frame, headers='keys', tablefmt='psql'), sep='')