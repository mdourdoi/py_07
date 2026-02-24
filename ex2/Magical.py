from typing import Dict, List, Any
from abc import ABC, abstractmethod


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, int]:
        raise NotImplementedError

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, int]:
        raise NotImplementedError
