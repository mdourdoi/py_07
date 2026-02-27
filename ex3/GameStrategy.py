from abc import ABC
from typing import Any, Dict, List
from ex0.Card import Card


class GameStrategy(ABC):

    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:
        raise NotImplementedError

    execute_turn.__isabstractmethod__ = True

    def get_strategy_name(self) -> str:
        raise NotImplementedError

    get_strategy_name.__isabstractmethod__ = True

    def prioritize_targets(self, available_targets: List[Card]) -> List[Any]:
        raise NotImplementedError

    prioritize_targets.__isabstractmethod__ = True
