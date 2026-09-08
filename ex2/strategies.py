from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability
from abc import ABC, abstractmethod


class InvalidStrategyError(Exception):
    ...


class BattleStrategy(ABC):
    def is_valid(self, creature: Creature) -> bool:
        ...
        
    def act(self, creature:Creature) -> str:
        ...
    

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, (TransformCapability))
    
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Battle error, aborting tournament: Invalid Creature"
                f" '{creature.name}' for this aggressive strategy")



class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return isinstance(creature, (HealCapability))
