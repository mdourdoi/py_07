from ex0.Card import Card
import random
from typing import Dict, List, Any
from math import ceil


class EmptyDeckError(Exception):
    pass


class Deck:

    def __init__(self, *cards: Card) -> None:
        temp_deck = []
        for card in cards:
            if not isinstance(card, Card):
                raise TypeError(f"{card} is not a valid card")
            temp_deck.append(card)
        self.deck: List[Card] = temp_deck

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.deck.append(card)
        else:
            raise TypeError(f"{card} is not a valid card")

    def remove_card(self, card_name: str) -> bool:
        temp_deck = [
            card for card in self.deck if not card.name == card_name]
        if len(self.deck) == len(temp_deck):
            return False
        self.deck = temp_deck
        return True

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) == 0:
            raise EmptyDeckError("Error : deck is empty")
        card = self.deck[0]
        self.deck.pop(0)
        return card

    def get_deck_stats(self) -> Dict[str, Any]:
        ret = {
            'total_cards': len(self.deck),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0}
        for card in self.deck:
            ret['avg_cost'] += card.cost
            ret[f'{card.type}s'] += 1
        if ret['total_cards'] != 0:
            ret['avg_cost'] = float(ceil(ret['avg_cost'] / ret['total_cards']))
        return ret
