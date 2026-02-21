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
            raise TypeError("Mana cannot be none")

        super().__init__(name, cost, rarity)
        self.atk_val: int = int(atk_val)
        self.def_val: int = int(def_val)
        self.cur_mana_val: int = int(cur_mana_val)

    def attack(self, target: Any) -> Dict:
        target_name = getattr(target, 'name', str(target))
        return {'attacker': self.name,
            'target': target_name,
            'damage': self.atk_val,
            'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = max(0, incoming_damage - self.def_val)
        damage_blocked = min(incoming_damage, self.def_val)
        return {'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': True}

    def get_combat_stats(self) -> Dict:
        return {'attack': self.atk_val, 'defense': self.def_val}

    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        return {'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4}

    def channel_mana(self, amount: int) -> Dict:
        self.cur_mana_val += amount
        return {'channeled': amount,
            'total_mana': self.cur_mana_val}

    def get_magic_stats(self) -> Dict:
        return {'mana': self.cur_mana_val}

    def play(self, game_state: Dict) -> Dict:
        return {'card_played': self.name,
            'mana_used': self.cost}
