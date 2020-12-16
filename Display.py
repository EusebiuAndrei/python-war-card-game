import pygame

from Card import Card

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))

sprites = {'back': pygame.image.load('sprites/back.png')}
for path in Card.paths:
    sprites[path.split('/')[1].split('.')[0]] = pygame.image.load(path)


def compute_position(surface, percentages):
    xPercentage, yPercentage = percentages
    display_width_pos = display_width * xPercentage
    display_height_pos = display_height * yPercentage

    surface_width_center = surface.get_width() // 2
    surface_height_center = surface.get_height() // 2

    x = display_width_pos - surface_width_center
    y = display_height_pos - surface_height_center

    return x, y


def is_inside(pos, surface_pos, surface):
    pos_x, pos_y = pos
    surface_pos_x, surface_pos_y = surface_pos
    img_width = surface.get_width()
    img_height = surface.get_height()

    if surface_pos_x <= pos_x <= surface_pos_x + img_width and surface_pos_y <= pos_y <= surface_pos_y + img_height:
        return True

    return False


def display_image(img, percentages):
    xPercentage, yPercentage = percentages
    position = compute_position(img, (xPercentage, yPercentage))
    gameDisplay.blit(img, position)


def display_text(text, percentages):
    xPercentage, yPercentage = percentages
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(text, True, black)
    gameDisplay.blit(text, compute_position(text, (xPercentage, yPercentage)))


def display_game(computer, human):
    display_text(f"Cpu's score: {computer.score}", computer.positions['text'])
    display_image(computer.image, computer.positions['image'])
    display_text(f"Your score: {human.score}", human.positions['text'])
    display_image(human.image, human.positions['image'])
    display_text(f"Number of remaining cards: {Card.nr_of_cards - (computer.score + human.score)}", (0.5, 0.85))
