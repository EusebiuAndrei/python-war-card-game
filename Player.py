class Player:
    def __init__(self, name, cards, image):
        self.name = name
        self.cards = cards
        self.score = 0
        self.image = image


    def get_first_card(self, nr_of_cards_to_ignore):
        nr_of_cards = len(self.cards)

        if nr_of_cards > nr_of_cards_to_ignore:
            return

        used_cards = self.cards[:nr_of_cards_to_ignore + 1]
        cards = self.cards[nr_of_cards_to_ignore:]

        return cards.pop(0), used_cards

    def add_cards(self, cards):
        self.cards = self.cards + cards
