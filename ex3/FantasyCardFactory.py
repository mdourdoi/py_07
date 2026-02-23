# FantasyCardFactory.py
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int |
                        None = None) -> CreatureCard:
        dragon = CreatureCard("Fire Dragon", 5, "Rare", 7, 6)
        gobelin = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        wizard = CreatureCard("Ice Wizard", 4, "Rare", 3, 4)
        weakling = CreatureCard("Weakling", 1, "Common", 1, 1)
        if isinstance(name_or_power, int):
            if name_or_power == 5:
                return dragon
            if name_or_power == 4:
                return wizard
            if name_or_power == 2:
                return gobelin
        if isinstance(name_or_power, str):
            if name_or_power.capitalize() == 'Dragon':
                return dragon
            if name_or_power.capitalize() == 'Wizard':
                return wizard
            if name_or_power.capitalize() == 'Gobelin':
                return gobelin
        return weakling

    def create_spell(self, name_or_power: str |
                     int | None = None) -> SpellCard:
        bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
        fireball = SpellCard("Fireball", 4, "Uncommon", "damage")
        shard = SpellCard("Ice Shard", 2, "Common", "damage")
        fizzle = SpellCard("Fizzle", 0, "Common", "buff")
        if isinstance(name_or_power, int):
            if name_or_power == 4:
                return fireball
            if name_or_power == 3:
                return bolt
            if name_or_power == 2:
                return shard
        if isinstance(name_or_power, str):
            if name_or_power.capitalize() == 'Bolt':
                return bolt
            if name_or_power.capitalize() == 'Fireball':
                return fireball
            if name_or_power.capitalize() == 'Shard':
                return shard
        return fizzle

    def create_artifact(self, name_or_power: str | int |
                        None = None) -> ArtifactCard:
        crystal = ArtifactCard(
            "Mana Crystal", 2, "Common", 5,
            "Permanent: +1 mana per turn")
        ring = ArtifactCard(
            "Ring of Wisdom", 4, "Rare", 4,
            "Permanent: Draw an extra card each turn")
        staff = ArtifactCard(
            "Staff of Elements", 6, "Legendary", 7,
            "Permanent: +1 spell damage")
        empty_artifact = ArtifactCard(
            "Nothing", 0, "Common", 1, "Permanent: Do nothing")

        if isinstance(name_or_power, int):
            if name_or_power == 4:
                return ring
            if name_or_power == 6:
                return staff
            if name_or_power == 2:
                return crystal
        if isinstance(name_or_power, str):
            if name_or_power.capitalize() == 'Ring':
                return ring
            if name_or_power.capitalize() == 'Crystal':
                return crystal
            if name_or_power.capitalize() == 'Staff':
                return staff
        return empty_artifact
