from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy, AggressiveStrategy,
    DefensiveStrategy, InvalidStrategyError)


Warrior = tuple[CreatureFactory, BattleStrategy]


def run_tournament(warriors: list[Warrior]) -> None:
    print("*** Tournament ***")
    print(f"{len(warriors)} opponents involved")

    for i, (factory1, strat1) in enumerate(warriors):
        for factory2, strat2 in warriors[i + 1:]:
            c1 = factory1.create_base()
            c2 = factory2.create_base()
    
            print("\n* Battle *")
            print(f"{c1.describe()}\nvs.\n{c2.describe()}\nnow fight!")
    
            try:
                strat1.act(c1)
                strat2.act(c2)
            except InvalidStrategyError as e:
                print(e)
                return


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    heal_fact = HealingCreatureFactory()
    transform_fact = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([
        (flame_fact, normal_strat),
        (heal_fact, defensive_strat)
    ])

    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament([
        (flame_fact, aggressive_strat),
        (heal_fact, defensive_strat)
    ])

    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    run_tournament([
        (aqua_fact, normal_strat),
        (heal_fact, defensive_strat),
        (transform_fact, aggressive_strat)
    ])
