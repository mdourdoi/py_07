from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print()
    print("=== DataDeck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()

    platform = TournamentPlatform()
    dragon = TournamentCard(
        "Fire Dragon", 5, "Rare", 8, 4, 14, 0, 0, 1200, "dragon_001")
    wizard = TournamentCard(
        "Ice Wizard", 4, "Rare", 6, 3, 12, 0, 0, 1150, "wizard_001")

    print(platform.register_card(dragon))
    print(platform.register_card(wizard))

    print("Creating tournament match...")
    match_result = platform.create_match(dragon.card_id, wizard.card_id)
    print(f"Match result: {match_result}")
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    i = 1
    for card in leaderboard:
        print(
            f"{i}. {card.name} - Rating: {card.calculate_rating()} "
            f"({card.wins}-{card.losses})")
        i += 1
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f"Unexpected error: {cur_error}")
