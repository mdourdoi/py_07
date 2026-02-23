from abc import ABC, abstractmethod
from typing import Any, Dict, List
from ex0.Card import Card


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_strategy_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Card]) -> List[Any]:
        raise NotImplementedError
