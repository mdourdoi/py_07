from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict, Any


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            atk_val: int,
            def_val: int,
            hp_val: int,
            wins: int,
            losses: int,
            base_rating: int,
            card_id: str) -> None:
        try:
            if int(atk_val) <= 0:
                raise ValueError(f'{atk_val} is not a valid attack input')
        except ValueError:
            raise ValueError(f'{atk_val} is not a valid attack input')

        try:
            if int(def_val) < 0:
                raise ValueError(f'{def_val} is not a valid attack input')
        except ValueError:
            raise ValueError(f'{def_val} is not a valid attack input')

        try:
            if int(hp_val) < 0:
                raise ValueError(f'{hp_val} is not a valid health input')
        except ValueError:
            raise ValueError(f'{hp_val} is not a valid health input')

        try:
            if int(wins) < 0:
                raise ValueError(f'{wins} is not a valid wins input')
        except ValueError:
            raise ValueError(f'{wins} is not a valid wins input')

        try:
            if int(losses) < 0:
                raise ValueError(f'{losses} is not a valid losses input')
        except ValueError:
            raise ValueError(f'{losses} is not a valid losses input')

        try:
            if int(base_rating) < 0:
                raise ValueError(f'{base_rating} is not a valid rating input')
        except ValueError:
            raise ValueError(f'{base_rating} is not a valid rating input')

        super().__init__(name, cost, rarity)
        self.atk_val: int = int(atk_val)
        self.def_val: int = int(def_val)
        self.hp_val: int = int(hp_val)
        self.wins: int = int(wins)
        self.losses: int = int(losses)
        self.base_rating: int = int(base_rating)
        self.card_id: str = str(card_id)

    def play(self, game_state: Dict[Any, Any]) -> Dict[str, Any]:
        ret = {}
        ret['card_played'] = self.name
        ret['mana_used'] = self.cost
        ret['effect'] = 'Card played in the tournament'
        return ret

    def attack(self, target: Any) -> Dict[str, Any]:
        target_name = getattr(target, 'name', str(target))
        return {'attacker': self.name,
                'target': target_name,
                'damage': self.atk_val}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_taken = max(0, incoming_damage - self.def_val)
        damage_blocked = min(incoming_damage, self.def_val)
        return {'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': damage_taken <= self.hp_val}

    def get_combat_stats(self) -> Dict[str, Any]:
        return {'attack': self.atk_val, 'defense': self.def_val}

    def calculate_rating(self) -> int:
        return self.base_rating + self.wins * 16 - self.losses * 16

    def update_wins(self, wins: int) -> None:
        try:
            if int(wins) <= 0:
                raise ValueError(f'{wins} is not a valid wins input')
        except ValueError:
            raise ValueError(f'{wins} is not a valid wins input')
        self.wins += int(wins)

    def update_losses(self, losses: int) -> None:
        try:
            if int(losses) <= 0:
                raise ValueError(f'{losses} is not a valid losses input')
        except ValueError:
            raise ValueError(f'{losses} is not a valid losses input')
        self.losses += int(losses)

    def get_rank_info(self) -> Dict[str, Any]:
        ret = dict()
        ret['Interfaces'] = '[' + \
            ', '.join(['Card', 'Combatable', 'Rankable']) + ']'
        ret['Rating'] = self.calculate_rating()
        ret['Record'] = f'{self.wins}-{self.losses}'
        return ret
