from typing import Any, Dict, List, Tuple
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: List[Card]) -> List[Any]:
        weakest_opp = None
        for card in available_targets:
            if weakest_opp is None or card.health < weakest_opp.health:
                weakest_opp = card
        return ['Enemy Player', weakest_opp]

    @staticmethod
    def get_lowest_creature(
            hand: List[Card]) -> Tuple[int, CreatureCard | None]:
        lowest_cost = None
        i = 0
        index = 0
        for card in hand:
            if isinstance(card, CreatureCard):
                if lowest_cost is None or card.cost < lowest_cost.cost:
                    lowest_cost = card
                    index = i
            i += 1
        return [index, lowest_cost]

    @staticmethod
    def get_lowest_damage_spell(
            hand: List[Card]) -> Tuple[int, SpellCard | None]:
        lowest_cost = None
        i = 0
        index = 0
        for card in hand:
            if isinstance(card, SpellCard):
                if card.effect_type == 'damage':
                    if lowest_cost is None or card.cost < lowest_cost.cost:
                        lowest_cost = card
                        index = i
            i += 1
        return [index, lowest_cost]

    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:
        hand_cpy = hand

        played = []
        mana_used = 0
        damage = 0
        index, lowest_creature = self.get_lowest_creature(hand_cpy)
        if lowest_creature is not None:
            played.append(lowest_creature.name)
            mana_used += lowest_creature.cost
            damage += lowest_creature.attack
            hand_cpy.pop(index)
        index, lowest_spell = self.get_lowest_damage_spell(hand_cpy)
        if lowest_spell is not None:
            played.append(lowest_spell.name)
            mana_used += lowest_spell.cost
            damage += lowest_spell.cost
            hand_cpy.pop(index)

        targets = self.prioritize_targets(battlefield)[:1]

        return {'cards_played': played,
                'mana_used': mana_used,
                'targets_attacked': targets,
                'damage_dealt': damage}
