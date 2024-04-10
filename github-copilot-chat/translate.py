import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    """
    Represents a deck of playing cards.
    """

    def __init__(self):
        self.cards = []
        self.populate_deck()

    def populate_deck(self):
        """
        Populates the deck with a standard set of playing cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Deals a card from the deck.
        Returns:
            Card: The dealt card, or None if the deck is empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    hand = []
    for _ in range(5):
        card = deck.deal()
        if card:
            hand.append(card)

    print("Your hand:")
    for card in hand:
        print(f"{card.value} of {card.suit}")
