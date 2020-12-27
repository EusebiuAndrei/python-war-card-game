import pygame
import Display
from Card import Card
from Game import Game, Status


def main(images):
    game = Game(images)
    Card.print_cards(game.players[0].cards)


if __name__ == "__main__":
    game = Game(Display.sprites)

    pygame.display.set_caption("War card game")
    clock = pygame.time.Clock()

    crashed = False

    buttonText = ''
    if game.status == Status.RoundStarted:
        buttonText = "Start Round"
    elif game.status == Status.RoundFinished:
        buttonText = "Finish Round"

    myButton = Display.get_button_pos_and_dim(buttonText, (0.5, 0.8), (10, 5))

    start_round = Display.get_button_pos_and_dim("Start Round", (0.35, 0.8), (10, 5))
    next_round = Display.get_button_pos_and_dim("Finish Round", (0.65, 0.8), (10, 5))
    print(start_round)
    print(game.status)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.status == Status.RoundFinished:
                    if Display.is_inside(event.pos, myButton[0], myButton[1]):
                        game.status = Status.RoundStarted
                elif game.status == Status.RoundStarted:
                    if Display.is_inside(event.pos, myButton[0], myButton[1]):
                        game.status = Status.Choosing
                elif game.status == Status.Comparing:
                    if Display.is_inside(event.pos, myButton[0], myButton[1]):
                        game.status = Status.RoundFinished

            # print("EVENT: ", event)
        # print("AAAAA")
        print(game.status)

        # automatic transitions
        if game.status == Status.Choosing and game.players[0].picked_card != '' and game.players[1].picked_card != '':
            game.status = Status.Comparing

        # State
        if game.status == Status.RoundStarted:
            game.players[0].show_card_back()
            game.players[1].show_card_back()

        if game.status == Status.Choosing:
            game.players[0].pick_card(0)
            game.players[0].image = game.players[0].picked_card.image
            game.players[1].pick_card(0)
            game.players[1].image = game.players[1].picked_card.image

        if game.status == Status.RoundFinished:
            game.reward_winner_of_round()
            game.players[0].delete_used_cards()
            game.players[1].delete_used_cards()

        Display.gameDisplay.fill(Display.white)
        Display.display_game(game)
        # pygame.draw.rect(Display.gameDisplay, Display.red, (150, 450, 100, 50))
        # Display.display_text()
        # Display.display_button("sasdas", (0.5, 0.5), (20, 20))

        pygame.display.update()
        clock.tick(60)