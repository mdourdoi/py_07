from ex0 import CreatureCard
from ex1 import ArtifactCard, SpellCard, Deck, EmptyDeckError

if __name__ == "__main__":
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5)
    lightning_bolt = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="damage")
    mana_crystal = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Common",
        durability=5,
        effect="Permanent: +1 mana per turn")

    print()
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    deck = Deck(lightning_bolt, mana_crystal, fire_dragon)
    try:
        print(f'Deck stats: {deck.get_deck_stats()}')
        print()

        print('Drawing and playing cards:')
        print()
        while deck.deck:
            card = deck.draw_card()
            print('Drew:', card.name)
            print('Play result:', card.play({}))
            print()
    except EmptyDeckError as cur_error:
        print(f'Error: {cur_error}')

    print('Polymorphism in action: Same interface, different card behaviors!')
