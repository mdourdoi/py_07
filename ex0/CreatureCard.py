from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int) -> None:
        try:
            int(attack) > 0
        except ValueError:
            raise ValueError(f"{attack} is not a valid attack value")
        try:
            int(health) > 0
        except ValueError:
            raise ValueError(f"{health} is not a valid health value")

        super().__init__(name, cost, rarity)
        self.type = 'creature'
        self.attack: int = int(attack)
        self.health: int = int(health)

    def attack_target(self, target: "CreatureCard") -> Dict:
        if not isinstance(target, CreatureCard):
            raise TypeError(f"{target} is not a CreatureCard")
        ret: Dict = {}
        ret['attacker'] = self.name
        ret['target'] = target.name
        ret['damage_dealt'] = self.attack
        ret['combat_resolved'] = True
        return ret

    def play(self, game_state: Dict) -> Dict:
        ret: Dict = {}
        ret['card_played'] = self.name
        ret['mana_used'] = self.cost
        ret['effect'] = 'Creature summoned to the battlefield'
        return ret
