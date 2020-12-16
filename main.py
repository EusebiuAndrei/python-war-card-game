from Card import Card


def main():
    cards = Card.get_shuffled_cards()
    Card.print_cards(cards)
    game = Game()
    Card.print_cards(game.players[0].cards)


if __name__ == "__main__":
    # main()
    import pygame

    pygame.init()

    display_width = 800
    display_height = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("War card game")
    clock = pygame.time.Clock()

    card_back_img = pygame.image.load('sprites/blue_back.png')
    card2 = pygame.image.load('sprites/2C.png')

    card_width = card_back_img.get_width()
    card_height = card_back_img.get_height()

    def compute_position(xPercentage, yPercentage, img_to_show):
        display_width_pos = display_width * xPercentage
        display_height_pos = display_height * yPercentage

        card_img_width_center = img_to_show.get_width() // 2
        card_img_height_center = img_to_show.get_height() // 2

        x = display_width_pos - card_img_width_center
        y = display_height_pos - card_img_height_center

        return x, y

    state_computer_image = card_back_img
    state_computer_pos = compute_position(0.5, 0.5, state_computer_image)
    state_computer_score = 0
    state_human_image = card_back_img
    state_human_score = 0

    def card(xPercentage, yPercentage, card_img):
        position = compute_position(xPercentage, yPercentage, card_img)
        gameDisplay.blit(card_img, position)

    def is_inside(pos, img_pos, img_to_show):
        pos_x, pos_y = pos
        img_pos_x, img_pos_y = img_pos
        img_width = img_to_show.get_width()
        img_height = img_to_show.get_height()

        if img_pos_x <= pos_x <= img_pos_x + img_width and img_pos_y <= pos_y <= img_pos_y + img_height:
            return True

        return False

    def message_display(text):
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(text, True, black)
        gameDisplay.blit(text, compute_position(0.5, 0.2, text))

    crashed = False

    to_display = card_back_img

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                print(is_inside(event.pos, state_computer_pos, state_computer_image))
                if is_inside(event.pos, state_computer_pos, state_computer_image):
                    to_display = card2

            # print("EVENT: ", event)
        gameDisplay.fill(white)
        message_display(f"Score {state_computer_score}")
        card(0.5, 0.5, to_display)

        pygame.display.update()
        clock.tick(60)