import Display


class Player:
    def __init__(self, name, cards, image, positions):
        self.name = name
        self.cards = cards
        self.score = 0
        self.image = image
        self.positions = positions
        self.used_cards = []
        self.picked_card = ''
        self.former_picked_card = ''

    def get_image_pos(self):
        return Display.compute_position(Display.get_dimension(self.image), self.positions['image'])

    def delete_picked_card(self):
        if self.picked_card == '':
            return

        self.former_picked_card = self.picked_card
        self.picked_card = ''

    def delete_used_cards(self):
        if self.picked_card == '':
            return

        self.used_cards = []

    def show_card_back(self):
        if self.image == Display.sprites['back']:
            return

        self.image = Display.sprites['back']

    def pick_card(self, take_former):
        nr_of_cards_to_ignore = 0
        if self.former_picked_card and take_former:
            nr_of_cards_to_ignore = self.former_picked_card.power + 2

        nr_of_cards = len(self.cards)

        if nr_of_cards <= nr_of_cards_to_ignore:
            nr_of_cards_to_ignore = nr_of_cards - 1

        self.used_cards += self.cards[:nr_of_cards_to_ignore + 1]
        self.cards = self.cards[nr_of_cards_to_ignore + 1:]
        self.picked_card = self.used_cards[-1]

    def add_cards(self, cards):
        self.cards = self.cards + cards
