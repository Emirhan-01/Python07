from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, c_type: str) -> None:
        self.name = name
        self.type = c_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", c_type="Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", c_type="Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", c_type="Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", c_type="Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
