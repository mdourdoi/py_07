from typing import Dict, Any, List
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
            cur_hp: int,
            combat_type: str,
            cur_mana_val: int) -> None:
        try:
            test = int(atk_val) > 0
            if not test:
                raise ValueError(f"{atk_val} is not a valid attack value")
        except ValueError:
            raise ValueError(f"{atk_val} is not a valid attack value")
        except TypeError:
            raise TypeError("Attack cannot be None")

        try:
            test = int(def_val) > 0
            if not test:
                raise ValueError(f"{def_val} is not a valid defense value")
        except ValueError:
            raise ValueError(f"{def_val} is not a valid defense value")
        except TypeError:
            raise TypeError("Defense cannot be None")

        try:
            test = int(cur_mana_val) > 0
            if not test:
                raise ValueError(f"{cur_mana_val} is not a valid mana value")
        except ValueError:
            raise ValueError(f"{cur_mana_val} is not a valid mana value")
        except TypeError:
            raise TypeError("Mana cannot be None")

        try:
            test = int(cur_hp) > 0
            if not test:
                raise ValueError(f"{cur_hp} is not a valid health value")
        except ValueError:
            raise ValueError(f"{cur_hp} is not a valid health value")
        except TypeError:
            raise TypeError("Health cannot be None")

        super().__init__(name, cost, rarity)
        self.atk_val: int = int(atk_val)
        self.def_val: int = int(def_val)
        self.cur_hp: int = int(cur_hp)
        self.combat_type: str = str(combat_type)
        self.cur_mana_val: int = int(cur_mana_val)

    def attack(self, target: Any) -> Dict[str, Any]:
        target_name = getattr(target, 'name', str(target))
        return {'attacker': self.name,
                'target': target_name,
                'damage': self.atk_val,
                'combat_type': self.combat_type}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_taken = max(0, incoming_damage - self.def_val)
        damage_blocked = min(incoming_damage, self.def_val)
        return {'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': damage_taken <= self.cur_hp}

    def get_combat_stats(self) -> Dict[str, Any]:
        return {'attack': self.atk_val, 'defense': self.def_val}

    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        return {'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': 4}

    def channel_mana(self, amount: int) -> Dict[str, int]:
        try:
            if int(amount) < 0:
                raise ValueError()
        except ValueError:
            raise ValueError(f"{amount} is not a valid amount to channel")
        self.cur_mana_val += amount
        return {'channeled': amount,
                'total_mana': self.cur_mana_val}

    def get_magic_stats(self) -> Dict[str, int]:
        return {'mana': self.cur_mana_val}

    def play(self, game_state: Dict[Any, Any]) -> Dict[str, Any]:
        return {'card_played': self.name,
                'mana_used': self.cost}
