from ex0 import AquaFactory, CreatureFactory, FlameFactory


def factory_test(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolution = factory.create_evolved()
    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolution.describe())
    print(evolution.attack())

def battle_test(f_one: CreatureFactory, f_two: CreatureFactory) -> None:
    pokemon_one = f_one.create_base()
    pokemon_two = f_two.create_base()
    print("Testing battle")
    print(pokemon_one.describe())
    print(" vs.")
    print(pokemon_two.describe())
    print(" fight!")
    print(pokemon_one.attack())
    print(pokemon_two.attack())

def test_start() -> None:
    f_factory = FlameFactory()
    a_factory = AquaFactory()
    factory_test(f_factory)
    print()
    factory_test(a_factory)
    print()
    battle_test(f_factory, a_factory)

test_start()
