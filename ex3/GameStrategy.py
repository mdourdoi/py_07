from abc import ABC
from typing import Any, Dict, List
from ex0.Card import Card


class GameStrategy(ABC):

    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:
        raise NotImplementedError

    def get_strategy_name(self) -> str:
        raise NotImplementedError

    def prioritize_targets(self, available_targets: List[Card]) -> List[Any]:
        raise NotImplementedError
