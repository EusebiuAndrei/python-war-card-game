from Card import Card
from Player import Player


class Game:
    def __init__(self):
        cards = Card.get_shuffled_cards()

        players = []
        players[0] = Player('Computer', cards[:Card.nr_of_cards // 2])
        players[1] = Player('You', cards[Card.nr_of_cards // 2:])

        self.players = players

    def attack(self):
        computer_card, used_computer_cards = self.players[0].get_first_card(0)
        human_card, used_human_cards = self.players[1].get_first_card(0)

        used_cards = []

        while computer_card == human_card:
            used_cards += used_computer_cards + used_human_cards

            nr_of_cards_to_ignore = computer_card[0].power + 2
            if computer_card[0].name == 'A':
                nr_of_cards_to_ignore = 11

            computer_card, used_computer_cards = self.players[0].get_first_card(nr_of_cards_to_ignore)
            human_card, used_human_cards = self.players[1].get_first_card(nr_of_cards_to_ignore)

        if computer_card.power > human_card.power:
            self.players[0].add_cards(used_cards)
        else:
            self.players[1].add_cards(used_cards)

        if len(self.players[0].cards) == 0 or len(self.players[1].cards) == 0:
            return True
        return False