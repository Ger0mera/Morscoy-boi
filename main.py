#1) создать класс менеджер всей игры(хранение игровых полей, логика поочередности ходов, хранение класса объекта ии)
#
#2) класс игрового поля(матрица состояния, возможность изменять состояния ячеек матрицы, отображение
#
#3) класс корабль(размер корабля, координаты корбаля, расположение побитых клеток корабля, направление корабля
#
#4) класс вектора(координаты x y, векторные операции)

import random


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, number: int | float) -> 'Vector':
        return Vector(self.x * number, self.y * number)


class Ship:
    def __init__(self, size: int, position: Vector, direction: Vector):
        self.size = size
        self.position = position
        self.direction = direction

    def check_collision(self, point: Vector) -> bool:
        for i in range(self.size):
            ship_pos = self.position + (self.direction * i)
            if ship_pos.x == point.x and ship_pos.y == point.y:
                return True
        return False


class PlayingField:
    def __init__(self, size: int, ships: list[Ship] = None):
        self.size = size
        self.matrix = [["." for _ in range(size)] for _ in range(size)]
        self.ships = ships if ships else []

    def generation(self, size: int):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            pos = Vector(x, y)
            dirs = [Vector(0, 1), Vector(0, -1), Vector(1, 0), Vector(-1, 0)]
            direction = random.choice(dirs)

            if self.can_place_ship(size, pos, direction):
                ship = Ship(size, pos, direction)
                self.ships.append(ship)
                self.mark_ship_on_field(ship)
                break

    def can_place_ship(self, size: int, position: Vector, direction: Vector) -> bool:
        for i in range(size):
            ship_pos = position + (direction * i)
            if not (0 <= ship_pos.x < self.size and 0 <= ship_pos.y < self.size):
                return False
            if self.matrix[ship_pos.x][ship_pos.y] == "■":
                return False
            for s in self.ships:
                for cel in range(s.size):
                    other_pos = s.position + (s.direction * cel)
                    if abs(other_pos.x - ship_pos.x) == 1 or abs(other_pos.y - ship_pos.y) == 1:
                        return False
        return True

    def mark_ship_on_field(self, ship: Ship):
        for i in range(ship.size):
            pos = ship.position + (ship.direction * i)
            self.matrix[pos.x][pos.y] = "■"

    def generationfield(self):
        for i in range(1, 5):
            size = 5 - i
            for _ in range(i):
                self.generation(size)
                self.draw()
                print()

    def draw(self) -> None:
        for row in self.matrix:
            print(" ".join(row))


class ManagerGame:
    def __init__(self):
        self.field = PlayingField(10)
        self.field.generationfield()
        self.field.draw()


if __name__ == "__main__":
    game = ManagerGame()

