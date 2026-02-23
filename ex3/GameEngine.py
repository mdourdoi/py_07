from typing import Any, Dict, List
from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    @staticmethod
    def is_cardlist(data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for item in data:
            if not isinstance(item, Card):
                return False
        return True

    def __init__(
            self,
            factory: CardFactory | None = None,
            strategy: GameStrategy | None = None,
            hand: List[Card] = list(),
            battlefield: List[Card] = list()):
        if not (isinstance(factory, CardFactory) or factory is None):
            raise TypeError(f'{factory} is not a valid factory')
        if not (isinstance(strategy, GameStrategy) or strategy is None):
            raise TypeError(f'{strategy} is not a valid strategy')
        if not self.is_cardlist(hand):
            raise TypeError(f'{hand} is not a valid hand')
        if not self.is_cardlist(battlefield):
            raise TypeError(f'{battlefield} is not a valid hand')

        self.factory: CardFactory | None = factory
        self.strategy: GameStrategy | None = strategy
        self.hand: List[Card] = hand
        self.battlefield: List[Card] = battlefield
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = len(hand)

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if not (isinstance(factory, CardFactory) or factory is None):
            raise TypeError(f'{factory} is not a valid factory')
        if not (isinstance(strategy, GameStrategy) or strategy is None):
            raise TypeError(f'{strategy} is not a valid strategy')

        self.strategy = strategy
        self.factory = factory

    def set_example_hand(self) -> None:
        if self.factory is None:
            raise RuntimeError("Factory is not configured")
        self.hand = [self.factory.create_creature(5),
                     self.factory.create_creature(2),
                     self.factory.create_spell(3)]
        self.cards_created += 3

    def simulate_turn(self) -> Dict[str, Any] | None:
        if self.strategy is None:
            raise RuntimeError("Strategy is not defined")
        if len(self.hand) == 0:
            self.set_example_hand()
        mock_turn = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += mock_turn['damage_dealt']
        return mock_turn

    def get_engine_status(self) -> Dict[str, int | str]:
        status = dict()
        status['turns_simulated'] = self.turns_simulated
        status['strategy_used'] = self.strategy.get_strategy_name()
        status['total_damage'] = self.total_damage
        status['cards_created'] = self.cards_created
        return status

    def print_hand(self) -> None:
        print("[", end="")
        print(", ".join(
            f"{card.name} ({card.cost})" for card in self.hand), end="")
        print("]")
