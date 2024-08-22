#1) создать класс менеджер всей игры(хранение игровых полей, логика поочередности ходов, хранение класса объекта ии)
#
#2) класс игрового поля(матрица состояния, возможность изменять состояния ячеек матрицы, отображение
#
#3) класс корабль(размер корабля, координаты корбаля, расположение побитых клеток корабля, направление корабля
#
#4) класс вектора(координаты x y, векторные операции)

import random
from enum import Enum


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, number: int | float) -> 'Vector':
        return Vector(self.x * number, self.y * number)


class Ship:
    def __init__(self, size: int, position: Vector, direction: Vector):
        self.size = size
        self.position = position
        self.direction = direction
        self.modules = []
        self.is_alive = True

    def hit(self, point: Vector):
        if self.check_collision(point):
            if len(self.modules) < self.size:
                self.modules.append(point)
                return True
            self.is_alive = False
        return False

    def get_neighboor(self) -> list[Vector]:
        result = []
        ship_cells = set()
        for i in range(self.size):
            ship_pos = self.position + (self.direction * i)
            ship_cells.add(ship_pos)
            result + Ship.get_neighboorcell(ship_pos)
        result = set(result)
        result = result.difference(ship_cells)
        result = list(result)
        return result

    @staticmethod
    def get_neighboorcell(cell: Vector) -> list[Vector]:
        cells = []
        for i in range(cell.x - 1, cell.x + 2):
            for j in range(cell.y - 1, cell.y + 2):
                cells.append(Vector(i, j))
        return cells

    def check_collision(self, point: Vector) -> bool:
        for i in range(self.size):
            ship_pos = self.position + (self.direction * i)
            if ship_pos.x == point.x and ship_pos.y == point.y:
                return True
        return False


class State(Enum):
    SHIP = "■"
    VOID = "-"
    BITE = "X"


class PlayingField:
    def __init__(self, size: int, ships: list[Ship] = None):
        self.size = size
        self.matrix = [["." for _ in range(size)] for _ in range(size)]
        self.ships = ships if ships else []

    def mark_cell(self, state: State, point: Vector):
        self.matrix[point.x][point.y] = state.value

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
                    if abs(other_pos.x - ship_pos.x) + abs(other_pos.y - ship_pos.y) <= 2:
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
                print()

    def draw(self) -> None:
        abc = ""
        for i in range(ord("A"), ord("A") + self.size):
            abc += f"  {chr(i)}"
        print(abc.rjust(3 * self.size + 1))
        for i, row in enumerate(self.matrix):
            print(str(i + 1).ljust(2), end=" ")
            print("  ".join(row))


class Player:
    def __init__(self, size: int):
        self.field = PlayingField(size)
        self.enemy_field = PlayingField(size)

    def move(self, other: "Player", x: int, y: int):
        point = Vector(x, y)
        for i in other.field.ships:
            if i.hit(Vector(x, y)):
                self.enemy_field.mark_cell(State.BITE, point)
                other.field.mark_cell(State.BITE, point)
                if not i.is_alive:
                    result = i.get_neighboor()
                    for point in result:
                        self.enemy_field.mark_cell(State.VOID, point)
                        other.field.mark_cell(State.VOID, point)
                return
        self.enemy_field.mark_cell(State.VOID, point)
        other.field.mark_cell(State.VOID, point)


class ManagerGame:
    def __init__(self, size: int):
        self.player1 = Player(size)
        self.player2 = Player(size)
        self.winner = 0

    def start(self):
        self.player1.field.generationfield()
        self.player2.field.generationfield()
        self.player1.field.draw()
        self.player1.enemy_field.draw()

    def mainloop(self):
        while self.winner == 0:
            x, y = tuple(map(int, input("(x,y):").split()))
            self.player1.move(self.player2, x, y)


if __name__ == "__main__":
    game = ManagerGame(10)
    game.start()
    game.mainloop()
