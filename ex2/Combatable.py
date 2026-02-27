from typing import Dict, Any
from abc import ABC


class Combatable(ABC):

    def attack(self, target: Any) -> Dict[str, Any]:
        raise NotImplementedError

    attack.__isabstractmethod__ = True

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        raise NotImplementedError

    defend.__isabstractmethod__ = True

    def get_combat_stats(self) -> Dict[str, Any]:
        raise NotImplementedError

    get_combat_stats.__isabstractmethod__ = True
