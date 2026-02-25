from typing import Dict, Any
from abc import ABC


class Combatable(ABC):

    def attack(self, target: Any) -> Dict[str, Any]:
        raise NotImplementedError

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        raise NotImplementedError

    def get_combat_stats(self) -> Dict[str, Any]:
        raise NotImplementedError
