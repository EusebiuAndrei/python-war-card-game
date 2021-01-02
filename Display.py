import pygame

from Card import Card
from Game import Status

origins = {
    'C': 'Clubs',
    'S': 'Spades',
    'H': 'Hearts',
    'D': 'Diamonds'
}

names = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    '11': '11',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
    'A': 'Ace',
}

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
nice_blue = (0, 149, 255)

clock = pygame.time.Clock()

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))

sprites = {
    'back': pygame.image.load('sprites/back.png'),
    'shield': pygame.image.load('sprites/shield.png'),
    'sword_to_left': pygame.image.load('sprites/sword_to_left.png'),
    'sword_to_right': pygame.image.load('sprites/sword_to_right.png'),
}
for path in Card.paths:
    sprites[path.split('/')[1].split('.')[0]] = pygame.image.load(path)


def compute_position(surface, percentages):
    xPercentage, yPercentage = percentages
    display_width_pos = display_width * xPercentage
    display_height_pos = display_height * yPercentage

    surface_width, surface_height = surface
    # surface_width_center = surface.get_width() // 2
    # surface_height_center = surface.get_height() // 2
    surface_width_center = surface_width // 2
    surface_height_center = surface_height // 2

    x = display_width_pos - surface_width_center
    y = display_height_pos - surface_height_center

    return x, y


def is_inside(pos, surface_pos, surface_dimension):
    pos_x, pos_y = pos
    surface_pos_x, surface_pos_y = surface_pos
    # img_width = surface.get_width()
    # img_height = surface.get_height()
    surface_width, surface_height = surface_dimension

    if surface_pos_x <= pos_x <= surface_pos_x + surface_width and surface_pos_y <= pos_y <= surface_pos_y + surface_height:
        return True

    return False


def get_dimension(surface):
    img_width = surface.get_width()
    img_height = surface.get_height()
    return img_width, img_height


def display_image(img, percentages):
    xPercentage, yPercentage = percentages
    position = compute_position(get_dimension(img), (xPercentage, yPercentage))
    gameDisplay.blit(img, position)


def display_text(text, percentages, color=black):
    xPercentage, yPercentage = percentages
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(text, True, color)
    gameDisplay.blit(text, compute_position(get_dimension(text), (xPercentage, yPercentage)))


def get_button_pos_and_dim(text, percentages, padding):
    xPercentage, yPercentage = percentages
    xPadding, yPadding = padding
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(text, True, black)
    pos_x, pos_y = compute_position(get_dimension(text), (xPercentage, yPercentage))
    pos_x = pos_x - xPadding
    pos_y = pos_y - yPadding
    return (pos_x, pos_y), (text.get_width() + xPadding * 2, text.get_height() + yPadding * 2)


def display_button(text, percentages, padding):
    xPercentage, yPercentage = percentages
    xPadding, yPadding = padding
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(text, True, white)
    pos_x, pos_y = compute_position(get_dimension(text), (xPercentage, yPercentage))
    pos_x = pos_x - xPadding
    pos_y = pos_y - yPadding
    pygame.draw.rect(gameDisplay, nice_blue, (pos_x, pos_y, text.get_width() + xPadding * 2, text.get_height() + yPadding * 2))
    gameDisplay.blit(text, compute_position(get_dimension(text), (xPercentage, yPercentage)))


def compute_card_picked_message(card):
    return f"picked {names[card.name]} of {origins[card.origin]}"


def display_game(game):
    computer = game.players[0]
    human = game.players[1]

    if game.status == Status.RoundFinished:
        if game.roundWinner == 0:
            display_text(f"Cpu won round {game.nthRound - 1}", (0.5, 0.1))
            display_image(sprites['sword_to_right'], (0.5, 0.45))
        elif game.roundWinner == 1:
            display_text(f"You won round {game.nthRound - 1}", (0.5, 0.1))
            display_image(sprites['sword_to_left'], (0.5, 0.45))
        else:
            display_text("Equality", (0.5, 0.1))
            display_image(sprites['shield'], (0.5, 0.45))
    elif game.status == Status.Comparing:
        display_text(f"Cards picked", (0.5, 0.1))
        display_text(f"Cpu {compute_card_picked_message(computer.picked_card)}", (0.25, 0.72))
        display_text(f"You {compute_card_picked_message(human.picked_card)}", (0.75, 0.72))
    else:
        display_text(f"Round number {game.nthRound}", (0.5, 0.1))

    display_text(f"Cpu's score: {len(computer.cards)}", computer.positions['text'])
    display_image(computer.image, computer.positions['image'])
    display_text(f"Your score: {len(human.cards)}", human.positions['text'])
    display_image(human.image, human.positions['image'])


    buttonText = ''
    if game.status == Status.RoundStarted:
        buttonText = "Pick"
    elif game.status == Status.Choosing or game.status == Status.Comparing:
        buttonText = "Battle"
    elif game.status == Status.RoundFinished:
        buttonText = "Finish Round"

    if game.autoplayMode is False:
        display_button(buttonText, (0.5, 0.8), (10, 5))

    autoplayText = ''
    if game.autoplayMode:
        autoplayText = "Stop"
    else:
        autoplayText = "Autoplay"

    display_button(autoplayText, (0.9, 0.9), (10, 5))
    display_button("Back", (0.1, 0.9), (10, 5))
