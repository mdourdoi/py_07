from ex4.TournamentCard import TournamentCard
from typing import Dict, Any, List


class TournamentPlatform():

    def __init__(self) -> None:
        self.reg: Dict[str, TournamentCard] = dict()
        self.match_count: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if isinstance(card, TournamentCard):
            if card.card_id in self.reg.keys():
                return 'This id is already registered'
            self.reg[card.card_id] = card
            ret = ''
            ret += f'{card.name} (ID: {card.card_id}):\n'
            for key, value in card.get_rank_info().items():
                ret += f'- {key}: {value}\n'
            return ret
        return 'Please input a valid TournamentCard'

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        if not (card1_id in self.reg.keys()
                and card2_id in self.reg.keys()):
            return {'Match result': 'At least one card is not registered'}
        ret = dict()
        card1 = self.reg[card1_id]
        card2 = self.reg[card2_id]
        combat_done = False
        i = 1
        while not combat_done:
            if not card2.defend(i * card1.atk_val)['still_alive']:
                ret['winner'] = card1_id
                ret['loser'] = card2_id
                combat_done = True
            elif not card1.defend(i * card2.atk_val)['still_alive']:
                ret['winner'] = card2_id
                ret['loser'] = card1_id
                combat_done = True
            i += 1
        self.reg[ret['winner']].update_wins(1)
        self.reg[ret['loser']].update_losses(1)
        ret['winner_rating'] = self.reg[ret['winner']].calculate_rating()
        ret['loser_rating'] = self.reg[ret['loser']].calculate_rating()
        self.match_count += 1
        return ret

    def get_leaderboard(self) -> List[TournamentCard]:
        return sorted(self.reg.values(),
                      key=TournamentCard.calculate_rating,
                      reverse=True)

    def generate_tournament_report(self) -> Dict[str, Any]:
        ret = dict()
        ret['total_cards'] = len(self.reg)
        ret['matches_played'] = self.match_count
        ret['avg_rating'] = sum([card.calculate_rating()
                                for card in self.reg.values()])
        if len(self.reg) > 0:
            ret['avg_rating'] /= len(self.reg)
        ret['platform_status'] = 'active' if len(self.reg) > 0 else 'inactive'
        return ret
