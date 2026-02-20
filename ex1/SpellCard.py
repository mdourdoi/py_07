from ex0 import Card
from typing import Dict


class SpellCard(Card):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str) -> None:
        if str(effect_type) not in ('buff', 'debuff', 'heal', 'damage'):
            raise ValueError(f"{effect_type} is not a valid effect_type")
        super().__init__(name, cost, rarity)
        self.type: str = 'spell'
        self.effect_type: str = str(effect_type)

    def play(self, game_state: Dict) -> Dict:
        ret: Dict = {}
        ret['card_played'] = self.name
        ret['mana_used'] = self.cost
        ret['effect'] = self.effect_type
        return ret

    def resolve_effect(self, game_state: Dict) -> Dict:
        ret: Dict = {}
        ret['resolved'] = True
        ret['effect'] = self.effect_type
        return ret
