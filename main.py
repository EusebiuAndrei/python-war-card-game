import pygame
import Display
from Card import Card
from Game import Game, Status
from Player import PlayerType


def main(images):
    game = Game(images)
    Card.print_cards(game.players[0].cards)


if __name__ == "__main__":
    game = Game(Display.sprites)

    pygame.display.set_caption("War card game")
    clock = pygame.time.Clock()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.status == Status.Choosing and game.turn == 1:
                    if Display.is_inside(event.pos, game.players[1].get_image_pos(), game.players[1].image):
                        game.players[1].pick_card(0)
                        game.players[1].image = game.players[1].picked_card.image
                        game.turn = 0

            # print("EVENT: ", event)
        # print("AAAAA")
        if game.status == Status.Choosing and game.players[0].picked_card != '' and game.players[1].picked_card != '':
            game.status = Status.Comparing

        if game.status == Status.Comparing and (game.players[0].picked_card == '' or game.players[1].picked_card == ''):
            game.status = Status.RoundFinished
            game.players[0].image = Display.sprites['back']
            game.players[1].image = Display.sprites['back']

        if game.status == Status.Choosing and game.turn == 0:
            game.players[0].pick_card(0)
            game.players[0].image = game.players[0].picked_card.image
            game.turn = 1

        if game.status == Status.Comparing:
            round_winner = game.get_winner_for_round()
            game.players[0].clear_cards()
            game.players[1].clear_cards()

        if game.status == Status.RoundFinished:
            game.status = Status.Choosing

        Display.gameDisplay.fill(Display.white)
        Display.display_game(game.players[0], game.players[1])

        pygame.display.update()
        clock.tick(60)