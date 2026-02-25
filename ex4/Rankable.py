from abc import ABC
from typing import Dict, Any


class Rankable(ABC):

    def calculate_rating(self) -> int:
        raise NotImplementedError

    def update_wins(self, wins: int) -> None:
        raise NotImplementedError

    def update_losses(self, losses: int) -> None:
        raise NotImplementedError

    def get_rank_info(self) -> Dict[str, Any]:
        raise NotImplementedError
