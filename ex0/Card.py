from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        try:
            int(cost)
        except ValueError:
            raise ValueError(f"{cost} is not a valid cost value")

        if (rarity.capitalize()
                not in ("Common", "Uncommon", "Rare", "Legendary")):
            ret_error = f'{rarity} is not a rarity, must be '
            ret_error += '"Common", "Uncommon", "Rare" or "Legendary"'
            raise ValueError(ret_error)
        
        self.name: str = str(name)
        self.cost: int = int(cost)
        self.rarity: str = str(rarity)

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        raise NotImplementedError

    def get_card_info(self) -> Dict:
        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana
