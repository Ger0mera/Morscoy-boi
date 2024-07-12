#1) создать класс менеджер всей игры(хранение игровых полей, логика поочередности ходов, хранение класса объекта ии)
#
#2) класс игрового поля(матрица состояния, возможность изменять состояния ячеек матрицы, отображение
#
#3) класс корабль(размер корабля, координаты корбаля, расположение побитых клеток корабля, направление корабля
#
#4) класс вектора(координаты x y, векторные операции)

import random
class Vector():
    ...


class Vector():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, number: int | float) -> Vector:
        return Vector(self.x * number, self.y * number)


class Ship():
    def __init__(self, size: int, position: Vector, direction: Vector):
        self.size = size
        self.position = position
        self.direction = direction

    def check_collision(self, point: Vector) -> bool:
        if self.position.x <= point.x <= self.position.x + self.size * self.direction.x:
            if self.position.y <= point.y <= self.position.y + self.size * self.direction.y:
                return True
        return False


class PlayingField():
    def __init__(self, size, ships: list[Ship] = None):
        self.size = size
        row = [0 for i in range(size)]
        self.matrix = [row.copy() for i in range(size)]
        if ships:
            self.ships = ships
        else:
            self.ships = []
    def generation(self):
        x = random.randint(0, self.size)
        y = random.randint(0, self.size)
        pos = Vector(x, y)
        dirs = [Vector(0, 1), Vector(0, -1), Vector(1, 0), Vector(-1, 0)]
        i = random.randint(0, 3)
        dir = dirs[i]
        size = 2
        ship = Ship()


    def draw(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(self.matrix[i][j], sep='', end="")
            print()




class ManagerGame():
    def __init__(self):
        ...

