from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability



class InvalidStrategyError(Exception):
    ...


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature:Creature) -> None:
        ...
    

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        print(creature.describe())
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Battle error, aborting tournament: Invalid Creature"
                f" '{creature.name}' for this aggressive strategy")
        assert isinstance(creature, TransformCapability)
        print(creature.describe())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Battle error, aborting tournament: Invalid Creature"
                f" '{creature.name}' for this aggressive strategy")
        assert isinstance(creature, HealCapability)
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())
