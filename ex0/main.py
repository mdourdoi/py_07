from ex0 import CreatureCard


def main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    print("CreatureCard Info:")
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5)
    print(fire_dragon.get_card_info())
    print()

    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon.is_playable(6))
    print("Play result:", fire_dragon.play({}))
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    goblin_warrior = CreatureCard(
        name="Goblin Warrior",
        cost=1,
        rarity="Common",
        attack=2,
        health=1)
    print("Attack result:", fire_dragon.attack_target(goblin_warrior))
    print()

    print("Testing insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f'Error: {cur_error}')
