import Display


class PlayerType:
    computer = 0
    human = 1


class Player:
    def __init__(self, name, cards, image, positions):
        self.name = name
        self.cards = cards
        self.score = 0
        self.image = image
        self.positions = positions
        self.used_cards = []
        self.picked_card = ''

    def get_image_pos(self):
        return Display.compute_position(self.image, self.positions['image'])

    def clear_cards(self):
        self.used_cards = []
        self.picked_card = ''

    def pick_card(self, nr_of_cards_to_ignore):
        nr_of_cards = len(self.cards)

        if nr_of_cards <= nr_of_cards_to_ignore:
            nr_of_cards_to_ignore = nr_of_cards - 1

        self.used_cards = self.cards[:nr_of_cards_to_ignore + 1]
        self.cards = self.cards[nr_of_cards_to_ignore:]
        self.picked_card = self.cards.pop(0)

    def add_cards(self, cards):
        self.cards = self.cards + cards
