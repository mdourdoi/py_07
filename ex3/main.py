from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print()
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    try:
        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        engine = GameEngine()
        engine.configure_engine(factory, strategy)
    except (TypeError, ValueError, RuntimeError) as cur_error:
        print(f"Error while configuring engine: {cur_error}")
        return

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")
    print()

    print("Simulating aggressive turn...")
    engine.set_example_hand()
    print("Hand: ", end="")
    engine.print_hand()
    print()

    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    try:
        actions = engine.simulate_turn()
    except Exception as cur_error:
        print(f"Error while simulating turn: {cur_error}")
        return
    print(f"Actions: {actions}")
    print()

    print("Game Report:")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print(f"Unexpected error: {cur_error}")
