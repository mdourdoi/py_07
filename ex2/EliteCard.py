from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            atk_val: int,
            def_val: int,
            cur_mana_val: int) -> None:
        try:
            test = int(atk_val) > 0
            if not test:
                raise ValueError(f"{atk_val} is not a valid attack value")
        except ValueError:
            raise ValueError(f"{atk_val} is not a valid attack value")
        except TypeError:
            raise TypeError("Attack cannot be none")

        try:
            test = int(def_val) > 0
            if not test:
                raise ValueError(f"{def_val} is not a valid defense value")
        except ValueError:
            raise ValueError(f"{def_val} is not a valid defense value")
        except TypeError:
            raise TypeError("Defense cannot be none")

        try:
            test = int(cur_mana_val) > 0
            if not test:
                raise ValueError(f"{cur_mana_val} is not a valid mana value")
        except ValueError:
            raise ValueError(f"{cur_mana_val} is not a valid mana value")
        except TypeError:
            raise TypeError("Defense cannot be none")

        super().__init__(name, cost, rarity)
        self.atk_val: int = int(atk_val)
        self.def_val: int = int(def_val)
        self.cur_mana_val: int = int(cur_mana_val)

    def attack(self, target: Any) -> Dict:
        raise NotImplementedError

    def defend(self, incoming_damage: int) -> Dict:
        raise NotImplementedError

    def get_combat_stats(self) -> Dict:
        raise NotImplementedError

    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        raise NotImplementedError

    def channel_mana(self, amount: int) -> Dict:
        raise NotImplementedError

    def get_magic_stats(self) -> Dict:
        raise NotImplementedError
