from typing import Dict, List, Any
from abc import ABC


class Magical(ABC):

    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def channel_mana(self, amount: int) -> Dict[str, int]:
        raise NotImplementedError

    def get_magic_stats(self) -> Dict[str, int]:
        raise NotImplementedError
