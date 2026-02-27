from abc import ABC
from typing import Any, Dict
from ex0.Card import Card


class CardFactory(ABC):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        raise NotImplementedError

    create_creature.__isabstractmethod__ = True

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        raise NotImplementedError

    create_spell.__isabstractmethod__ = True

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        raise NotImplementedError

    create_artifact.__isabstractmethod__ = True

    def create_themed_deck(self, size: int) -> Dict[str, Card]:
        raise NotImplementedError

    create_themed_deck.__isabstractmethod__ = True

    def get_supported_types(self) -> Dict[str, Any]:
        raise NotImplementedError

    get_supported_types.__isabstractmethod__ = True
