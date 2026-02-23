from abc import ABC, abstractmethod
from typing import Any, Dict, List
from ex0.Card import Card


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:
        return NotImplementedError

    @abstractmethod
    def get_strategy_name(self) -> str:
        return NotImplementedError

    @abstractmethod
    def prioritize_target(self, available_targets: List[Card]) -> List[Any]:
        return NotImplementedError
