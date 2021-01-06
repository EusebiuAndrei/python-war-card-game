import pygame
import Display
from Game import Game, Status


def game_screen():
    game = Game(Display.sprites)

    isGameFinished = False

    buttonText = ''
    if game.status == Status.RoundStarted:
        buttonText = "Pick"
    elif game.status == Status.Comparing:
        buttonText = "Battle"
    elif game.status == Status.RoundFinished:
        buttonText = "Finish Round"

    myButton = Display.get_button_pos_and_dim(buttonText, (0.5, 0.8), (10, 5))

    autoplayText = ''
    if game.autoplayMode:
        autoplayText = "Stop"
    else:
        autoplayText = "Autoplay"

    autoplayButton = Display.get_button_pos_and_dim(autoplayText, (0.9, 0.9), (10, 5))

    back_button = Display.get_button_pos_and_dim("Back", (0.1, 0.9), (10, 5))

    message_end_time = pygame.time.get_ticks() + 1000  # display for 3 secondsz

    formerStatus = game.status
    while not isGameFinished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameFinished = True
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Display.is_inside(event.pos, myButton[0], myButton[1]):
                    if game.status == Status.RoundFinished:
                        game.status = Status.RoundStarted
                    elif game.status == Status.RoundStarted:
                        game.status = Status.Choosing
                    elif game.status == Status.Comparing:
                        game.status = Status.RoundFinished
                if Display.is_inside(event.pos, autoplayButton[0], autoplayButton[1]):
                    if game.autoplayMode is True:
                        game.autoplayMode = False
                    else:
                        game.autoplayMode = True
                if Display.is_inside(event.pos, back_button[0], back_button[1]):
                    isGameFinished = True

        current_time = pygame.time.get_ticks()
        if formerStatus != game.status:
            formerStatus = game.status

        if game.autoplayMode is True:

            if current_time > message_end_time:
                game.autoplay()
                message_end_time = pygame.time.get_ticks() + 1000  # display for 3 secondsz

        if game.status == Status.War:
            if current_time > message_end_time:
                game.status = Status.Choosing
                message_end_time = pygame.time.get_ticks() + 1000  # display for 3 secondsz

        game.run()

        Display.gameDisplay.fill(Display.white)
        Display.display_game(game)

        pygame.display.update()
        Display.clock.tick(60)

    return False


def home_screen():
    isGameExited = False

    start_button = Display.get_button_pos_and_dim('Start', (0.5, 0.45), (10, 5))
    exit_button = Display.get_button_pos_and_dim('Exit', (0.5, 0.55), (10, 5))

    while not isGameExited:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameExited = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Display.is_inside(event.pos, start_button[0], start_button[1]):
                    isGameExited = game_screen()
                elif Display.is_inside(event.pos, exit_button[0], exit_button[1]):
                    isGameExited = True

        Display.gameDisplay.fill(Display.white)
        Display.display_text(f"This a war card game", (0.5, 0.35))
        Display.display_button('Start', (0.5, 0.45), (10, 5))
        Display.display_button('Exit', (0.5, 0.55), (10, 5))

        pygame.display.update()
        Display.clock.tick(60)


def main():
    pygame.display.set_caption("War card game")
    home_screen()


if __name__ == "__main__":
    main()