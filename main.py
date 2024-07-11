#1) создать класс менеджер всей игры(хранение игровых полей, логика поочередности ходов, хранение класса объекта ии)
#
#2) класс игрового поля(матрица состояния, возможность изменять состояния ячеек матрицы, отображение
#
#3) класс корабль(размер корабля, координаты корбаля, расположение побитых клеток корабля, направление корабля
#
#4) класс вектора(координаты x y, векторные операции)
class Vector():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
class Ship():
    def __init__(self, size: int, position: Vector, direction: Vector):
        self.size = size
        self.position =  position
        self.direction = direction
class PlayingField():
    def __init__(self, size):
        self.size = size
#    size 10
#    row = [0 for i in range]
#    matrix = [row.copy() for i in range(size)]
#    def vectore(self, x: int, y:int):


class ManagerGame():
    def __init__(self):
        ...