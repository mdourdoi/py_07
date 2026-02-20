from typing import Dict
from abc import ABC, abstractmethod


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        raise NotImplementedError
