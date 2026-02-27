from abc import ABC
from typing import Dict, Any


class Rankable(ABC):

    def calculate_rating(self) -> int:
        raise NotImplementedError

    calculate_rating.__isabstractmethod__ = True

    def update_wins(self, wins: int) -> None:
        raise NotImplementedError

    update_wins.__isabstractmethod__ = True

    def update_losses(self, losses: int) -> None:
        raise NotImplementedError

    update_losses.__isabstractmethod__ = True

    def get_rank_info(self) -> Dict[str, Any]:
        raise NotImplementedError

    get_rank_info.__isabstractmethod__ = True
