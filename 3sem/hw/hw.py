class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = 16

    def update_count(self, val):
        if val > self._max_count or val < 0:
            raise ('Perepolnenie')


    def __imul__(self, num):
        self.update_count(num * self._count)
        self._count *= num
        return self

    def __iadd__(self, num):
        self.update_count(num + self._count)
        self._count += num
        return self

    def __isub__(self, num):
        self.update_count(self._count - num)
        self._count -= num
        return self

    def __mul__(self, num):
        return self._count * num

    def __add__(self, num):
        return self._count + num

    def __sub__(self, num):
        return self._count - num

    def __eq__(self, num):
        if self._count == num:
            return 1
        return 0

    def __lt__(self, num):
        if self._count < num:
            return 1
        return 0

    def __gt__(self, num):
        if self._count > num:
            return 1
        return 0

    def __ge__(self, num):
        if self._count >= num:
            return 1
        return 0

    def __le__(self, num):
        if self._count <= num:
            return 1
        return 0


it = Item()
print(it + 3)
print(it._count)
it -= 1
print(it._count)
print(it < 2)



class Fruit(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Food(Item):
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self._saturation = saturation

    def eatable(self):
        return self._saturation > 0


class Apple(Fruit, Food):
    def __init__(self, ripe=True, count=1, max_count=32, color='green', saturation=10):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color
        self._ripe = ripe

    def color(self):
        return self._color

    def eatable(self):
        return super().eatable and self._ripe


class Mandarin(Fruit, Food):
    def __init__(self, ripe=True, count=1, max_count=32, color='orange', saturation=5):
        super().__init__(ripe=ripe, count=count, max_count=max_count, saturation=saturation)
        self._color = color
        self._ripe = ripe

    def color(self):
        return self._color

    def eatable(self):
        return super().eatable and self._ripe


class Banana(Fruit, Food):
    def __init__(self, ripe=True, count=1, max_count=32, color='yellow', saturation=20):
        super().__init__(ripe=ripe, count=count, max_count=max_count, saturation=saturation)
        self._colot = color
        self._ripe = ripe

    def color(self):
        return self._color

    def eatable(self):
        return super().eatable and self._ripe


class Potato(Food):
    def __init__(self, fresh=True, count=5, max_count=64, color='brown', saturation=50):
        super().__init__(count=count, max_count=max_count, saturation=saturation)
        self._color = color
        self._fresh = fresh

    def color(self):
        return self._color

    def fresh(self):
        return self._fresh

    def eatable(self):
        return super().eatable and self._fresh


class Tomato(Food):
    def __init__(self, fresh=True, count=10, max_count=40, color='red', saturation=40):
        super().__init__(count=count, max_count=max_count, saturation=saturation)
        self._color = color
        self._fresh = fresh

    def color(self):
        return self._color

    def fresh(self):
        return self._fresh

    def eatable(self):
        return super().eatable and self._fresh


a = Apple()
print(a + 1)

class Inventory():
    def __init__(self, _length):
        self.length = _length
        self.inventory = self.length * [None]

    def info_elem(self, id):
        print('В ячейке', id, 'хранится', self.inventory[id].__class__.__name__, ':',  self.inventory[id].__dict__)

    def push_elem(self, id, elem):
        if isinstance(elem, Food) and elem.eatable():
            if self.inventory[id] is None:
                self.inventory[id] = elem
            else:
                print('Ячейка под номером', id, 'занята')
            return self
        else:
            print('Это нельзя положить')

    def sub_count_elem(self, id, num):
        name = self.inventory[id].__class__.__name__
        self.inventory[id] -= num
        if self.inventory[id]._count == 0:
            #self.inventory.pop(id)
            self.inventory[id] = None
            print(f'{name} больше нет')
        else:
            print('Теперь в ячейке', id, 'хранится', self.inventory[id]._count, name)

    def show_count_elem(self, id):
        print(self.inventory[id]._count)


a = Inventory(10)
apple = Apple(count = 5)
potato = Potato(count = 10)
potato2 = Potato(fresh=False, count = 4)
a.push_elem(3, potato2)
banana = Banana(ripe=False, count = 4)
a.push_elem(4, banana)
a.push_elem(1, apple)
a.push_elem(1, potato)
a.push_elem(2, potato)
a.info_elem(2)
a.sub_count_elem(2, 1)
a.sub_count_elem(1, 5)


