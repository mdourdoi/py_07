from ex0 import Card
from typing import Dict


class ArtifactCard(Card):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str) -> None:
        try:
            int(durability)
        except ValueError:
            raise ValueError(f"{durability} is not a valid durability")
        except TypeError:
            raise TypeError("Durability cannot be None")
        if str(effect)[:11] != "Permanent: ":
            raise ValueError(f"{effect} is not a valid effect")
        super().__init__(name, cost, rarity)
        self.type: str = 'artifact'
        self.durability: int = int(durability)
        self.effect: str = str(effect)

    def play(self, game_state: dict) -> Dict:
        ret: Dict = {}
        ret['card_played'] = self.name
        ret['mana_used'] = self.cost
        ret['effect'] = self.effect
        return ret

    def activate_ability(self) -> Dict:
        return {'effect': self.effect, 'activated': True}
