from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Type, List

def get_public_methods(cls: Type) -> List[str]:
    return [m for m in dir(cls) if not m.startswith('_') and callable(getattr(cls, m))]


if __name__ == "__main__":
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print(f"- Card: {get_public_methods(Card)}")
    print(f"- Combatable: {get_public_methods(Combatable)}")
    print(f"- Magical: {get_public_methods(Magical)}")
    print()
    
    print("Playing Arcane Warrior (Elite Card):")
    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 4)
    print()

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")
    print()

    print("Magic phase:")
    print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")
    print()

    print("Multiple interface implementation successful!")
