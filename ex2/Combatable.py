from typing import Dict, Any
from abc import ABC, abstractmethod


class Combatable(ABC):

    @abstractmethod
    def attack(self, target: Any) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        raise NotImplementedError
