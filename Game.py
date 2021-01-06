from Card import Card
from Player import Player


class Status:
    RoundStarted = 1
    Choosing = 2
    Comparing = 3
    RoundFinished = 4
    War = 5


class Game:
    def __init__(self, images):
        cards = Card.get_shuffled_cards(images)

        players = [
            Player('Computer',
                   cards[:Card.nr_of_cards // 2], images['back'], {'image': (0.25, 0.45), 'text': (0.25, 0.2)}),
            Player('You',
                   cards[Card.nr_of_cards // 2:], images['back'], {'image': (0.75, 0.45), 'text': (0.75, 0.2)})
        ]

        self.players = players
        self.status = Status.RoundStarted
        self.turn = 0
        self.nthRound = 1
        self.roundWinner = -1
        self.winner = -1
        self.autoplayMode = False

    def run(self):
        if len(self.players[0].cards) == 0 and len(self.players[1].cards) == 0 and self.players[0].picked_card.power == self.players[1].picked_card.power:
            self.winner = 2
        if len(self.players[0].cards) == Card.nr_of_cards:
            self.winner = 0
        elif len(self.players[1].cards) == Card.nr_of_cards:
            self.winner = 1

        # automatic transitions
        if self.status == Status.Choosing and self.players[0].picked_card != '' and self.players[1].picked_card != '':
            self.status = Status.Comparing

        if self.status == Status.RoundStarted:
            self.on_round_started()
        elif self.status == Status.Choosing:
            self.on_choosing()
        elif self.status == Status.RoundFinished:
            self.on_round_finished()

    def autoplay(self):
        if self.status == Status.RoundFinished:
            self.status = Status.RoundStarted
        elif self.status == Status.RoundStarted:
            self.status = Status.Choosing
        elif self.status == Status.Comparing:
            self.status = Status.RoundFinished

    def on_round_started(self):
        self.players[0].show_card_back()
        self.players[1].show_card_back()

    def on_choosing(self):
        take_former = self.roundWinner == -1
        self.players[0].pick_card(take_former)
        self.players[0].image = self.players[0].picked_card.image
        self.players[1].pick_card(take_former)
        self.players[1].image = self.players[1].picked_card.image

    def on_round_finished(self):
        self.reward_winner_of_round()

        if self.roundWinner == -1:
            self.status = Status.Choosing
            self.players[0].delete_picked_card()
            self.players[1].delete_picked_card()
        else:
            self.players[0].delete_used_cards()
            self.players[1].delete_used_cards()
            self.players[0].delete_picked_card()
            self.players[1].delete_picked_card()

    def reward_winner_of_round(self):
        if self.players[0].picked_card == '':
            return

        used_cards = self.players[0].used_cards + self.players[1].used_cards

        if self.players[0].picked_card.power > self.players[1].picked_card.power:
            self.players[0].add_cards(used_cards)
            self.roundWinner = 0
        elif self.players[0].picked_card.power < self.players[1].picked_card.power:
            self.players[1].add_cards(used_cards)
            self.roundWinner = 1
        else:
            self.roundWinner = -1

        self.nthRound = self.nthRound + 1