from Card import Card
from Player import Player


class Status:
    Choosing = 1
    Comparing = 2
    RoundFinished = 3


class Game:
    def __init__(self, images):
        cards = Card.get_shuffled_cards(images)
        # Card.print_cards(cards)

        players = [
            Player('Computer',
                   cards[:Card.nr_of_cards // 2], images['back'], {'image': (0.25, 0.5), 'text': (0.25, 0.2)}),
            Player('You',
                   cards[Card.nr_of_cards // 2:], images['back'], {'image': (0.75, 0.5), 'text': (0.75, 0.2)})
        ]

        self.players = players
        self.status = Status.Choosing
        self.turn = 0

    def attack(self):
        computer_card, used_computer_cards = self.players[0].pick_card(0)
        human_card, used_human_cards = self.players[1].pick_card(0)

        used_cards = []

        while computer_card == human_card:
            used_cards += used_computer_cards + used_human_cards

            nr_of_cards_to_ignore = computer_card[0].power + 2
            if computer_card[0].name == 'A':
                nr_of_cards_to_ignore = 11

            computer_card, used_computer_cards = self.players[0].pick_card(nr_of_cards_to_ignore)
            human_card, used_human_cards = self.players[1].pick_card(nr_of_cards_to_ignore)

        if computer_card.power > human_card.power:
            self.players[0].add_cards(used_cards)
        else:
            self.players[1].add_cards(used_cards)

        if len(self.players[0].cards) == 0 or len(self.players[1].cards) == 0:
            return True
        return False

    def get_winner_for_round(self):
        used_cards = self.players[0].used_cards + self.players[1].used_cards

        if self.players[0].picked_card.power > self.players[1].picked_card.power:
            self.players[0].add_cards(used_cards)
            self.players[0].score = self.players[0].score + len(used_cards)
        else:
            self.players[1].add_cards(used_cards)
            self.players[1].score = self.players[1].score + len(used_cards)