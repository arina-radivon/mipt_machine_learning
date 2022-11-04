import abc

"""Задача 1: Написать класс, содержащий информацию об игроке."""


class Player:
    id: int
    name: str
    scores: int
    games: list
    """Информация об игроке"""
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.scores: int = 0
        self.games: list = []

    def add_result(self, game_id: int, scores: int) -> None:
        """Добавляет id игры и суммирует очки"""
        self.games.append(game_id)
        self.scores += scores

    def get_mean(self) -> float:
        """Возвращает средний балл по сыгранным играм"""
        return self.scores/len(self.games)


"""Задача 2. Создать классы персонажей"""


class Creature:
    pass


class EarthCreature(Creature):
    pass


class Troll(EarthCreature):
    health_points = 100


class Elf(EarthCreature):
    health_points = 80


class SeaCreature(Creature):
    pass


class Mermaid(SeaCreature):
    health_points = 60


class Siren(SeaCreature):
    health_points = 75


class AirCreature(Creature):
    pass


class Dragon(AirCreature):
    health_points = 120


class Pegasus(AirCreature):
    health_points = 85


"""Задача 3: Написать классы использования способностей.
Использование физических ограничено числом count, использование магических
 неограничено, за использование добавляется 1 очко """


class Power(abc.ABC):
    def __init__(self, name, cost):
        self.abil = name
        self.cost = cost

    @abc.abstractmethod
    def use(self, player: Player):
        'Определяется в подклассах'


class PhysicalPower(Power):

    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost
        self.count = count

    def use(self, player: Player):

        if self.count > 0:
            self.count -= 1
            print(f'{player.name} used {self.name}')
            return

        if self.count == 0:
            print(f'{player.name} cannot use {self.name}')
            return


class MagicPower(Power):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def use(self, player: Player):
        player.scores += 1
        print(f'{player.name} used {self.name}')


if __name__ == '__main__':

    """TESTS"""
    p = Player(1, 'Bilbo')
    print(p.id)
    print(p.name)
    print(p.scores)
    print(p.games)

    p.add_result(15, 10)
    p.add_result(21, 5)
    print(p.scores)
    print(p.games)
    print(p.get_mean())

    x = Elf()
    print(isinstance(x, EarthCreature))
    print(isinstance(x, Creature))
    print(x.health_points)

    p = Player(1, 'Bilbo')
    t = PhysicalPower('teleport', 10, count=1)
    t.use(p)
    t.use(p)
    print(p.scores)

    b = MagicPower('black magic', 200)
    b.use(p)
    print(p.scores)
    b.use(p)
    print(p.scores)
